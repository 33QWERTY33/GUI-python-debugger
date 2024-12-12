from django.shortcuts import render

# Create your views here.
def diagram(request):
    return render(request, 'diagrammer/diagram.html')