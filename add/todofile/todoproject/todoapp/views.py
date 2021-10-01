from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm


# Create your views here.
def tests(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        names = request.POST.get('task', '')
        priorities = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        tasktable = Task(name=names, priority=priorities, date=date)
        tasktable.save()
    return render(request, "home.html", {'task': tasks})


# def detail(request):
#     tasks = Task.objects.all()
#     return render(request, 'detail.html', {'task': tasks})
def deleted(request, tid):
    t = Task.objects.get(id=tid)
    if request.method == 'POST':
        t.delete()
        return redirect('/')
    return render(request, 'delete.html')


def updation(request, taskid):
    ta = Task.objects.get(id=taskid)
    f = TodoForm(request.POST or None, instance=ta)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'ta': ta})
