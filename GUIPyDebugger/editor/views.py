import io
import json
import sys
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Display the text box for editing
@csrf_exempt
def editor(request):
    if request.method == "POST":

        output = ""
        # set output to empty string

        data = json.loads(request.body)
        # deserialize json object 

        code = data.get('code')
        # get the value under "code" key

        output_buffer = io.StringIO()
        # Create an in-memory buffer

        sys.stdout = output_buffer
        # redirect standard output to the in memory buffer

        try:
            # happy path
            exec(code)
            # execute the received code

            sys.stdout.flush()
            # ensure the in-memory buffer actually receives the data in stdout

            output = output_buffer.getvalue()
            # store in-memory buffer contents inside of output variable for display on GUI
            
        except Exception as e:
            output = str(e)
            # capture errors if interpreter raises one

        sys.stdout = sys.__stdout__
        # set stdout back to normal

        output = output.replace("\n", "<br>")

        return JsonResponse({"output": output})
        # return a JSON object storing the string results of the execution

    return render(request, 'editor/editor.html')