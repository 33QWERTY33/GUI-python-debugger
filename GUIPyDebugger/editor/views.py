import io
import json
import sys
from . import utils
import diagrammer.views as project_info

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def editor(request):
    if not project_info.entry_point_path:
        return render(request, "editor/no-entry-point.html")
    else:
        debug_shell = utils.Debugger(project_info.entry_point_path)
    # Create a programmatically controllable debugger instance

    if request.method == "POST":

        output = ""
        # set output to empty string

        data = json.loads(request.body)
        # deserialize json object 

        if data.get("handler") == "Code Executor":
            output_buffer = io.StringIO()
            # Redirect standard output to the in-memory buffer
            sys.stdout = output_buffer

            code = data.get('code')
            # get the value under "code" key

            output = exec(code)

            output = output_buffer.getvalue()
            output = output.replace("\n", "<br>")  # Replace newlines with HTML break tags

            sys.stdout = sys.__stdout__  # Restore stdout

            return JsonResponse({"output": output})
            # return a JSON object storing the string results of the execution
        if data.get("handler") == "PDB Command":
            command = data.get("pdb_command")
            # isolate the desired command

            output= debug_shell.execute_debug_cmd(command)

            return JsonResponse({"output": output})
            # return a JSON object storing the string results of the execution

    return render(request, 'editor/editor.html')