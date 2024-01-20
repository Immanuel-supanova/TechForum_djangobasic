from django.urls import path
from todo.views import home, tododetailview

urlpatterns = [
    path('', home, name="home"),
    path('todo/<int:id>/', tododetailview, name="todo_detail")
]