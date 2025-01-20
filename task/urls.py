from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uncompleted_tasks/', views.uncompleted_tasks, name='uncompleted_tasks'),
]