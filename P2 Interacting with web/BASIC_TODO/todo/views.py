from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    allofthem=TodoItem.objects.all()
    return render(request, 'todo.html',
    {
        'all_items':allofthem
    })

def addTodo(request):
    new_item=TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delTodo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo/')