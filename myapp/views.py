from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyects, Task
from .forms import CreateNewTask
# Create your views here.

def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title' : title
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    # proyects = list(Proyects.objects.values())
    projects = Proyects.objects.all()
    return render(request, 'projects.html', {
        'projects' : projects
    })  

def tasks(request):
    # task = Task.objects.get(title = title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html' , {
        'tasks' : tasks 
    })
    
def createTask(request):
    return render(request, 'create_tasks.html', {
        'form' : CreateNewTask
    })