from todoapp.forms import TaskForm, UpdateTaskForm
from django.forms import forms
from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

# Create your views here.
def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()

    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    count_uncompleted_todo =  count_todos - count_completed_todo

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task Created Successfully!')
            return redirect('/')
    else:
        form = TaskForm()
    context ={'todos': todos, 'form': form, 'count_todos': count_todos, 'count_completed_todo': count_completed_todo, 'count_uncompleted_todo': count_uncompleted_todo}
    return render(request, 'todo/index.html', context)

def update(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST,instance = todo)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task Updated Successfully!')
            return redirect('/')
         
    else:
        form = UpdateTaskForm(instance=todo)

    context = {
        'form': form

    }
    return render(request, 'todo/update.html', context)


def delete(request,pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, f'Task Deleted Successfully!')
        return redirect('/')
    return render(request, 'todo/delete.html')