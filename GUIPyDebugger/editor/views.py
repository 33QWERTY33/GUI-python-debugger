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

        data = json.loads(request.body)

        code = data.get('code')

        output_buffer = io.StringIO()

        sys.stdout = output_buffer

        try:
            exec(code)

            sys.stdout.flush()

            output = output_buffer.getvalue()
            
        except Exception as e:
            output = str(e)

        sys.stdout = sys.__stdout__
        
        return JsonResponse({"output": output})

    return render(request, 'editor/editor.html')