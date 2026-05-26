from django.shortcuts import render
from todo.models import Tasks

def home(request):
    tasks = Tasks.objects.filter(is_completed = False).order_by('-updated_at')
    completed_task =  Tasks.objects.filter(is_completed = True).order_by('updated_at')
    context = {
        'tasks' : tasks,
        'completed_task' : completed_task
    }
    return  render(request, 'home-todo.html',context)