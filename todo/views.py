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