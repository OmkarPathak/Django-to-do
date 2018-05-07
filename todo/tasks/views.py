from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect
from .models import TaskForm, Task, UsernameForm, Username
from django.template import RequestContext

# Create your views here.
def tasks(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST)
        if form.is_valid():
            user = Username.objects.get(username=request.COOKIES.get('username'))
            temp = form.save(commit=False)
            temp.username = user
            temp.save()
        tasks = Task.objects.filter(username__username=request.COOKIES.get('username')).order_by('priority')
        return render(request, 'tasks.html', {'form': form, 'tasks': tasks, 'user': user})
    else:
        if 'username' not in request.COOKIES:
            from django.utils.crypto import get_random_string
            unique_id = get_random_string(length=32)
            username = Username()
            username.username = unique_id
            username.save()
            response = redirect(reverse('tasks'))
            # 604800s = 1 week
            response.set_cookie('username', username, max_age=604800)
            return response
        # this is where GET request are accessed
        form = TaskForm()
        tasks = Task.objects.filter(username__username=request.COOKIES.get('username')).order_by('priority')
        user = Username.objects.filter(username=request.COOKIES.get('username'))
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks, 'user': user})

def delete(request, id):
    Task.objects.filter(id=id).delete()
    return redirect(reverse('tasks'))

def complete(request, id):
    task=Task.objects.get(id=id)
    if task.complete:
       task.complete = 0
    else:
        task.complete = 1
    task.save()
    return redirect('/')

def clear(request):
    Username.objects.filter(username=request.COOKIES['username']).delete()
    response = HttpResponseRedirect('/tasks/')
    response.delete_cookie('username')
    return response
