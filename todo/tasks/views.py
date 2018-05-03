from django.shortcuts import render
from .models import TaskForm

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        pass
    else:
        form = TaskForm()
    return render(request, 'tasks.html', {'form': form})

def add(request):
    return render(request, 'tasks.html')
