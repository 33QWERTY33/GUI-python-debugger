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
        sys.path.append(str(os.path.join(settings.STATICFILES_DIRS[0], "code_files", diagrammer.venv_path, "Lib", "site-packages")))
        
    # find some way to include the virtual environment directory!!

    module = utils.dynamic_import(entry_point_name, entry_point_path)
    # dynamic import logic

    submodules = module_info.get_submodules(code)

    info = {
        "submodules": submodules
    }

    return render(request, 'diagrammer/diagram.html', info)

