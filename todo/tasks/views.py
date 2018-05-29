from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from .models import TaskForm, Task, UsernameForm, Username
from django.template import RequestContext

# Create your views here.

def tasks(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST or None)
        if form.is_valid():
            user = Username.objects.get(username=request.COOKIES.get('username'))
            temp = form.save(commit=False)
            temp.username = user
            temp.save()
            form = TaskForm()
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

def check_user_validity(request):
    '''
    Check if user such user exists in Database 
    '''
   
    try:
        return Username.objects.get(username__exact=request.COOKIES["username"])
    except Exception:
        return False

def delete(request, id):
    if 'username' in request.COOKIES and check_user_validity(request):
        #now check if user trying to access this task actually created this task
        Task.objects.filter(id=id,username=Username.objects.get(username__exact=request.COOKIES["username"])).delete()
        return redirect(reverse('tasks'))
    else:
        return HttpResponse("You are not allowed to access this resource")

def complete(request, id):
    if 'username' in request.COOKIES and check_user_validity(request):
        try:
            task=Task.objects.get(id=id,username=Username.objects.get(username__exact=request.COOKIES["username"]))
            if task.complete:
                task.complete = 0
            else:
                task.complete = 1
            task.save()
            return redirect('/')
        except Exception:
            return HttpResponse("Sorry You are not allowed to access This task ")
    else:
        return HttpResponse("You are not allowed to access this resource")



def clear(request):
    Username.objects.filter(username=request.COOKIES['username']).delete()
    response = HttpResponseRedirect('/tasks/')
    response.delete_cookie('username')
    return response
