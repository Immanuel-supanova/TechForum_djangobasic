from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def deadline(self):
        return f'{self.date} {self.time}'
    
    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'pk': self.pk})
    
    