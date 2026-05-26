from django.shortcuts import get_object_or_404, redirect, render
from .models import Tasks

# Create your views here.

def add_task(request):
    task = request.POST['task']
    Tasks.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request,pk):
    old_task = get_object_or_404(Tasks,pk=pk)
    if request.method == 'POST':
        old_task.task = request.POST['task']
        old_task.save()
        return redirect('home')
    else:
        context = {
            'task' : old_task,
        }
    return render(request, 'edit.html', context)