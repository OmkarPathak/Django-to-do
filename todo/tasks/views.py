from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'tasks.html')

def add(request):
    return render(request, 'tasks.html')
