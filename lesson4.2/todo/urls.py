from django.urls import path
from todo.views import HomeView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', TodoCreateView.as_view(), name="todo_create"),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name="todo_update"),
    path('<int:pk>/', TodoDetailView.as_view(), name="todo_detail"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name="todo_delete"),
]
