import inspect
import pkgutil
import re

def get_submodules(code):
    submodules = []
    chars_to_remove = len(r"static\code_files") + 1
    for _, modname, _ in pkgutil.walk_packages(path=code.__path__, prefix=code.__name__ + '.'):
        submodules.append(modname[chars_to_remove:]) #removing the static directory from the beginning
    
    return submodules

def get_blocks(code):
    src_code = inspect.getsource(code).split("\n")
    blocks = []
    line_numbers = []
    docstrings = []
    is_func = []
    line_no = 0
    while True:
        block = inspect.getblock(src_code[line_no:])
        # slice the source code, get the first block, append it
        if len(block) > 1:
            # getblock returns '' or just the line if there is no detected block so there is always 1 element
            blocks.append(block)
            line_numbers.append(line_no + 1)
            docstrings.append(get_docstring(block)[0])
            is_func.append(block[0][:3] == "def")
            # re.findall returns a list for each match, we only want the first docstring
            
        line_no += len(block)
        # I only want to find top level blocks
        if len(src_code[line_no:]) <= 0:
            break
        # If no lines are left, then break

    return filter(lambda block: block[1][0][0] not in "#'\"", zip(line_numbers, blocks, docstrings, is_func))
    # filters out comments and doc strings

def get_members(function):
    return inspect.getmembers(function)

def get_locals(code):
    pass

def get_attrs(code):
    pass

def get_docstring(code):
    src_code = "".join(code)
    docstring_match = re.findall(r'("""(.*?)"""|\'\'\'(.*?)\'\'\')', src_code, re.DOTALL)
    
    if len(docstring_match) == 0:
        docstring_match.append("")
        # if no match is found just add an empty string
    return docstring_match