from django.shortcuts import render, redirect

from .models import *                           # this is imported from models before forms.py

from .forms import *                            # this is imported form forms after forms.py

# Create your views here.

def index(request):
    tasks = Task.objects.all()                  # we are importing everything from models.

    form = TaskForm()                           # imported from forms

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}      # we are creating a dict and giving tasks data into dict / form is imported into templates
    return render(request, 'index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id = pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'delete.html', context)