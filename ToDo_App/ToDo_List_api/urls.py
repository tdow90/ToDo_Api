from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoView.as_view()),
    path('<int:pk>/', views.ToDoUpdate.as_view()),
    path('completed/', views.CompleteToDoView.as_view())
]

