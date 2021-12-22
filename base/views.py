from django import forms
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Tasks
from .forms import NewTask




def home_page(request):
    context = {
        'tasks' : Tasks.objects.all()
    }
    return render(request, 'base/home.html', context)

def base_task(request):
    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            # process form data
            obj = Tasks()
            obj.task_name = form.cleaned_data['task_name']
            obj.task_content = form.cleaned_data['task_content']
            obj.save()
            return redirect('home-page')
    else:
        form = NewTask()
    return render(request, 'base/base_task.html', {'form':form})

# <app>/<Model>_<viewtype>.html
class TasksListView(ListView):
    model = Tasks
    template_name = 'base/home.html'
    context_object_name = 'tasks'
    ordering = ['-date_created']

class TasksDetailView(DetailView):
    model = Tasks

class TasksUpdateView(UpdateView):
    model = Tasks
    fields = ['task_name', 'task_content']

class TasksDeleteView(DeleteView):
    model = Tasks
    success_url = '/'