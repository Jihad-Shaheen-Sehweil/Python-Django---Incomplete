from django.urls import path
from .views import TasksListView, TasksDetailView, TasksUpdateView, TasksDeleteView
from . import views

urlpatterns = [
    path('', TasksListView.as_view(), name='home-page'),
    path('task/<int:pk>/', TasksDetailView.as_view(), name='task-detail'),
    path('base_task/', views.base_task, name='base_task'),
    path('task/<int:pk>/update/', TasksUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TasksDeleteView.as_view(), name='task-delete'),
]