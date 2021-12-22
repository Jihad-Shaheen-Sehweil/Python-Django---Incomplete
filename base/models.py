from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.urls import reverse

class Tasks(Model): # this class call is the creation table of Post
    task_name = models.CharField(max_length=100) # this the colomn of title
    task_content = models.TextField(default="")
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})