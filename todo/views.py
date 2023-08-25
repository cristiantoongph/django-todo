from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task

def addTask(request):
  # print(request.POST['task'])
  task = request.POST['task']
  #create object or task
  Task.objects.create(task=task)
  return redirect('home')

def mark_as_done(request, pk):
  task = get_object_or_404(Task, pk=pk)
  # edit current task then save
  task.is_completed = True
  task.save()
  return redirect('home')

def mark_as_undone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = False
  task.save()
  return redirect('home')

def edit_task(request, pk):
  get_task = get_object_or_404(Task, pk=pk)
  #CHECK IF POST REQUEST OR NOT
  if request.method == "POST":
    #capture new task and store it in a variable
    new_task = request.POST['task']
    # update existing task
    get_task.task = new_task
    get_task.save()
    return redirect('home')
  else:
    #to prefill the input element with task data
    context = {
      'get_task': get_task,
    }
  return render(request, 'edit_task.html', context)

def delete_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.delete()
  return redirect('home')