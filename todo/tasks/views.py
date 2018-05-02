from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'base.html', {'name': 'root'})

def add(request):
    return render(request, 'base.html', {'name': 'add'})
