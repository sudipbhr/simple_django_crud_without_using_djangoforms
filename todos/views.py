from django.shortcuts import render, redirect
from .models import task
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        a = request.POST['work']
        status = 0
        data = task(item=a, status=status)
        data.save()
        messages.success(request,"Tasks added successfully.")
    tasks= task.objects.all()
    context ={
        'tasks':tasks
    }
    template = 'todos/index.html'
    
    return render(request, template, context)

def edit(request, id):
    t= task.objects.get(id=id)
    if request.method == 'POST':
        a = request.POST['work']
        t= task.objects.get(id=id)
        t.item =a
        t.save()
        messages.success(request,"Tasks updated successfully.")
        return redirect('index')
    context={
        't': t
    }
    template = 'todos/edit.html'
    
    return render(request, template, context)


def delete(request, id):
    data= task.objects.get(id=id);
    data.delete()
    messages.error(request,"Tasks delete successfully.")
    tasks= task.objects.all()
    context ={
        'tasks':tasks
    }
    template = 'todos/index.html'
    return render(request, template, context)

def pending(request, id):
    tasks= task.objects.get(id=id);
    if tasks.status == 0:
        tasks.status =1
    else:
        tasks.status = 0
    messages.warning(request,"Tasks status changed successfully.")
    tasks.save()
    context={}
    template = 'todos/index.html'
    return redirect('index')

