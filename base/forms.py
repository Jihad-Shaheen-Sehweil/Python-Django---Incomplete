from django import forms
from .models import Tasks

  
# creating a form 
class NewTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_name', 'task_content']
