from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    detail = models.TextField(blank='True', null='True')
    created_date = models.DateTimeField(auto_now_add="True")
    due_date = models.DateField(blank = 'True', null='True')
    completed = models.BooleanField()

    def __str__(self):
        return self.title
    