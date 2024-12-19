import sys
from django.shortcuts import render
import static.code_files as code
from . import module_info, utils
import diagrammer
import os
import GUIPyDebugger.settings as settings
# If errors arise from this line it's probably because this folder wasn't created properly

# Create your views here.
def diagram(request):
    entry_point_string = "#ENTRY\n"
    module_path = code.__path__[0]

    entry_point_name, entry_point_path = utils.find_entry_point(module_path, entry_point_string)
    # Entry point finding logic
    
    if entry_point_name == None:
        return render(request, 'diagrammer/no-entry-point.html')
        # If no entry point is found

    sys.path.append(module_path)

    if diagrammer.venv_path != "":
        sys.path.append(str(os.path.join(
                settings.STATICFILES_DIRS[0], 
                "code_files", diagrammer.venv_path,
                "Lib",
                "site-packages")))
        # this includes packages installed in a virtual environment

    try:
        module = utils.dynamic_import(entry_point_name, entry_point_path)
        # dynamic import logic
    except SyntaxError as e:
        return render(request, "diagrammer/syntax-error.html", {
            "error_msg": e.msg, 
            "error_text": e.text,
            "error_file": e.filename,
            "error_line": e.lineno})
    except FileNotFoundError as e:
        return render(request, "diagrammer/syntax-error.html", {
                "error_msg": e.msg, 
                "error_text": e.text,
                "error_file": e.filename,
                "error_line": e.lineno})
        # this page is for syntax error, create more informational page later
    except ImportError as e:
            return render(request, "diagrammer/syntax-error.html", {
                "error_msg": e.msg, 
                "error_text": e.text,
                "error_file": e.filename,
                "error_line": e.lineno})
        # this page is for syntax error, create more informational page later

    submodules = module_info.get_submodules(code)

    blocks = module_info.get_blocks(module)

    # The goal is to eventually marry these data structures into one hierarchy
    # Currently the submodules are sorted alphabetically
    # Their contents on the diagram window are unrelated to them

    info = {
        "submodules": submodules,
        "blocks": blocks
    }

    return render(request, 'diagrammer/diagram.html', info)

