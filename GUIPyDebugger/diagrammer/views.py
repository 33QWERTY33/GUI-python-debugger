from django.shortcuts import render
import static.code_files as code
from . import module_info, utils
import diagrammer
# If errors arise from this line it's probably because this folder wasn't created properly

# Create your views here.
def diagram(request):
    entry_point_string = "#ENTRY\n"
    module_path = code.__path__[0]

    entry_point_name, _ = utils.find_entry_point(module_path, entry_point_string)
    # Entry point finding logic
    
    if entry_point_name == None:
        return render(request, 'diagrammer/no-entry-point.html')
        # If no entry point is found

    info = module_info.master_dict_constructor(code)

    return render(request, 'diagrammer/diagram.html', info)