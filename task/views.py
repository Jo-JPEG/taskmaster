from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    uncompleted_tasks = Task.objects.filter(completed=False).order_by('due_date')
    completed_tasks = Task.objects.filter(completed=True).order_by('due_date')
    return render(request, 'index.html', {'uncompleted_tasks': uncompleted_tasks, 'completed_tasks': completed_tasks})
