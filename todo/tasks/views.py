from django.shortcuts import render
from .models import TaskForm, Task

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'form': form, 'tasks': tasks})
    else:
        # this is where GET request are accessed
        form = TaskForm()
        tasks = Task.objects.all()
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks})

def add(request):
    return render(request, 'tasks.html')
