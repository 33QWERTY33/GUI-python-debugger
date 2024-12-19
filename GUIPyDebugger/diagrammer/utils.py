import importlib
import os
import sys

def find_entry_point(code_files_path, entry_point_string):

    entry_point_path, entry_point_name = None, None

    for dirpath, _, filenames in os.walk(code_files_path):
    # traverse replicated file tree
        for filename in filenames:
            if ".py" in filename and filename[-1] != "c":
                # ignore .pyc files
                with open(os.path.join(dirpath, filename), "r") as file:
                    first_line = file.readline()
                    if first_line == entry_point_string:
                        file_contents = ''.join(file.readlines())
                        entry_point_path = os.path.join(dirpath, filename)
                        entry_point_name = filename
            if entry_point_path != None:
                break
        if entry_point_path != None:
            break
    
    return entry_point_name, entry_point_path

def dynamic_import(entry_point_name, entry_point_path):
    spec = importlib.util.spec_from_file_location(entry_point_name, entry_point_path)

    module = importlib.util.module_from_spec(spec)

    sys.modules[entry_point_name] = module

    try:
        spec.loader.exec_module(module)
    except ImportError as e:
        print(f"Error while loading module {entry_point_name}: {e}")
        print("Modules with code other than python cannot be dynamically imported such as numpy")
    except FileNotFoundError as e:
        print(f"Error while loading module {entry_point_name}: {e}")
        print("Hard coded file paths do not work yet")

    return module