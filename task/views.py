from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def uncompleted_tasks(request):
    tasks = Task.objects.filter(completed=False).order_by('due_date')
    return render(request, 'uncompleted_tasks.html', {'tasks': tasks})

