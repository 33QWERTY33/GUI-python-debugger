import ast
import inspect
import os
import pkgutil
import re

def get_submodules(code):
    '''
    Used to grab submodules from code_files package (it's a package cause __init__.py is inserted by default)
    '''
    submodules = []
    chars_to_remove = len(r"static\code_files") + 1
    # can't think of a fancier way to specify this value...
    for module_finder, modname, ispackage in pkgutil.walk_packages(path=code.__path__, prefix=code.__name__ + '.'):
        submodules.append((modname[chars_to_remove:], module_finder.path, ispackage)) #removing the static directory from the beginning
    
    return submodules

def get_blocks(name, path):
    with open(os.path.join(path, name + ".py"), "r") as python_file:
        # fixing some weirdness with how pkgutil.walk_packages represents module names
        src_code = python_file.read().split("\n")
        
    blocks = []
    line_numbers = []
    docstrings = []
    is_func = []
    is_class = []
    line_no = 0
    while True:
        try:
            block = inspect.getblock(src_code[line_no:])
            # slice the source code, get the first block, append it
        except Exception as e:
            print("[ERROR] likely EOF token causing trouble")
            break

        if len(block) > 1:
            # getblock returns '' or just the line if there is no detected block so there is always 1 element
            line_numbers.append(line_no + 1)
            docstrings.append(get_docstring(block))
            is_func.append(block[0][:3] == "def")
            is_class.append(block[0][:5] == "class")

            if is_class[-1] == True:
                in_class_body = True
                line_no += len(block)
                while in_class_body:
                    next_block = inspect.getblock(src_code[line_no:])
                    if "\t" in next_block[0] or "    " in next_block[0] or "     " in next_block[0]:
                        line_no += len(next_block)
                        for line in next_block:
                            block.append(line)
                    else:
                        blocks.append(block)
                        # append the class
                        in_class_body = False
                # this is because inspect.getblock treats different methods in a class as different blocks
                # this method is almost more trouble than it's worth...
            elif is_func[-1] == True:
                line_no += len(block)
                blocks.append(block)
            else:
                if len(src_code[line_no:]) <= 0:
                    break
                line_no += len(block)
        else:
            if len(src_code[line_no:]) <= 0:
                break
            else:
                line_no += len(block)
        # If no lines are left, then break


    return list(zip(line_numbers, blocks, docstrings, is_func, is_class))
    # filters out comments and doc strings

def get_docstring(code):
    src_code = "\n".join(code)
    docstring_match = re.findall(r'"""(.*?)"""', src_code, re.DOTALL)

    if len(docstring_match) == 0:
        docstring_match = re.findall(r"'''(.*?)'''", src_code, re.DOTALL)
    # this catches ''' and """ docstrings
    

    if len(docstring_match) == 0:
        docstring_match.append("")
        # if no match is found just add an empty string

    docstring_match = docstring_match[0]

    return docstring_match

def get_local_var_names(block):
    tree = ast.parse(block)

    var_names = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    var_names.append(target.id)

    return var_names

def get_class_attrs(block):
    tree = ast.parse(block)

    class_attrs = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    class_attrs.append(target.id)
    return class_attrs

def get_inst_attrs(block):
    tree = ast.parse(block)

    inst_attrs = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Attribute):
                    inst_attrs.append(target.attr)

    return inst_attrs

def get_methods(block):
    tree = ast.parse(block)

    methods = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            methods.append(node.name)

    return methods

def master_dict_constructor(code):
    info = {"modules": []}
    submodules = get_submodules(code)

    for name, path, ispkg in submodules:
        if ispkg:
            pass
        else:
            name_slice = name[name.rfind(".") + 1:] if name.rfind(".") != -1 else name
            # names are stored like folder.folder.file.py
            # need to remove the folders as that info is already in the path
            blocks = get_blocks(name_slice, path)

            functions = list(filter(lambda blockdata: blockdata[3] == True, blocks))
            classes = list(filter(lambda blockdata: blockdata[4] == True, blocks))

            # Get the blocks that specify a function
            module = {"name": name,
                      "path": path,
                      "functions": [
                          {"line_no": function[0],
                           "signature": function[1][0][4:-1],
                           "docstring": function[2],
                           "locals": get_local_var_names("\n".join(function[1])),
                           "contents": "\n".join(function[1])}
                       for function in functions],
                      "classes": [
                          {"line_no": c[0],
                           "signature": c[1][0][6:],
                           "docstring": c[2],
                           "instance_attrs": get_inst_attrs("\n".join(c[1])),
                           "class_attrs": get_class_attrs("\n".join(c[1])),
                           "methods": get_methods("\n".join(c[1])),
                           "contents": "\n".join(c[1])}
                       for c in classes]}
            
            info["modules"].append(module)

    return info