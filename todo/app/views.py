from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import TodoForm,EditTodo

# Create your views here.
def todo(request):
    if request.method =='POST':
        form =TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form=TodoForm()  
    tasks=Todo.objects.all()
    d={'tasks':tasks,'form':form}
    return render(request,'todo.html',d)

def  Edit(request,id):
    task =get_object_or_404(Todo, id=id)
    if request.method=='POST':
        form = EditTodo(request.POST,instance=task)
        if form.is_valid():
          form.save()
          return redirect('todo')
    else:
        form=EditTodo(instance=task)
        d={'form':form}
        return render(request,'update.html',d)
def Delete(request,id):
    task =get_object_or_404(Todo, id=id)
    if request.method=='POST':
        task.delete()
        return redirect('todo')
    return render(request,'delete_conf.html',{'task':task})
        


