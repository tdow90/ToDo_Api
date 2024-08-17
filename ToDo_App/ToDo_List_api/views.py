from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Todo
from .serializers import ToDoSerializer


# Create your views here.
#List all Todo objects that are from a specific user
class ToDoView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        # Optionally filter the queryset based on the user
        user = self.request.user
        return Todo.objects.filter(user=user, completed=False).order_by('due_date')
    
#List all Todo's that are completed
class CompleteToDoView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        # Optionally filter the queryset based on the user
        user = self.request.user
        return Todo.objects.filter(user=user, completed=True).order_by('-created_date')

# Class to update or delete, only for the user.
class ToDoUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        # Optionally filter the queryset based on the user
        user = self.request.user
        return Todo.objects.filter(user=user)