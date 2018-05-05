from django.shortcuts import render, redirect
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

def delete(request, id):
    Task.objects.filter(pk=id).delete()
    return redirect('/tasks/')


def complete(request, id):
	task=Task.objects.get(pk=id)
	task.complete = 1
	task.save()
	return redirect('/tasks/') 
