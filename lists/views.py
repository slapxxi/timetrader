from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task, List


def index(request):
  tasks = Task.objects.all()
  return render(request, 'lists.html', {'tasks': tasks})


def show(request):
  tasks = Task.objects.all()
  return render(request, 'list.html', {'tasks': tasks})


def new(request):
  list_ = List.objects.create()
  Task.objects.create(description=request.POST.get('task_description'), list=list_)

  return redirect('/lists/unique/')
