from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Todo(models.Model):
    """"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title
