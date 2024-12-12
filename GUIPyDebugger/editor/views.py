from django.shortcuts import render

# Create your views here.

# Display the text box for editing
def editor(request):
    return render(request, 'editor/editor.html')