from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import ToDoSerializer
#from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Didn't add, but could just add LoginRequiredMixin, this would only show page if you are logedIn. Also, should filter only specific users Todo's 
class ToDoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

