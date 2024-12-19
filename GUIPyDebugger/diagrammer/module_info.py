import inspect
import pkgutil

def get_submodules(code):
    submodules = []
    chars_to_remove = len(r"static\code_files") + 1
    for _, modname, _ in pkgutil.walk_packages(path=code.__path__, prefix=code.__name__ + '.'):
        submodules.append(modname[chars_to_remove:]) #removing the static directory from the beginning
    
    return submodules

def get_globals(code):
    return list(code.__dict__.keys())

def get_members(function):
    return inspect.getmembers(function)

def get_params(function):
    return inspect.getargs(function)

def get_locals(code):
    pass

def get_blocks(code):
    pass

def get_attrs(code):
    pass

def get_docstrings(code):
    pass