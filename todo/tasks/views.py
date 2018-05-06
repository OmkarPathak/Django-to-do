from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect
from .models import TaskForm, Task, UsernameForm, Username
from django.template import RequestContext

# Create your views here.
def tasks(request):
    if 'username' not in request.COOKIES:
        return redirect(reverse('username'))
    try:
        user = Username.objects.get(username=request.COOKIES['username'])
    except (KeyError, Username.DoesNotExist):
        return redirect(reverse('clear_username'))
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.username = user
            temp.save()
        tasks = Task.objects.filter(username=user).order_by('priority')
        return render(request, 'tasks.html', {'form': form, 'tasks': tasks})
    else:
        # this is where GET request are accessed
        form = TaskForm()
        tasks = Task.objects.filter(username=user).order_by('priority')
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks, 'user': user})

def username(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = UsernameForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            tasks = Task.objects.filter(username__username=username).order_by('priority')
            user = Username.objects.get(username=username)
            form = TaskForm()
            response = redirect(reverse('tasks'))
            response.set_cookie('username', username)
            return response
        else:
            if 'username' in request.COOKIES:
                return redirect(reverse('tasks'))
            return render(request, 'tasks.html', {'username_form':form})
    else:
        print(request.COOKIES)
        if 'username' in request.COOKIES:
            return redirect(reverse('tasks'))
        # this is where GET request are accessed
        form = UsernameForm()
    return render(request, 'tasks.html', {'username_form':form})

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
    response = HttpResponseRedirect('/username/')
    response.delete_cookie('username')
    return response
