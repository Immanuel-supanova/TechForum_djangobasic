from django.urls import path

from todo.views import homeview, todocreateview, tododetailview, todoupdateview, tododeleteview

urlpatterns = [
    path('', homeview, name="home"),
    path('create/', todocreateview, name="todo_create"),
    path('update/<int:id>/', todoupdateview, name="todo_update"),
    path('<int:id>/', tododetailview, name="todo_detail"),
    path('delete/<int:id>/', tododeleteview, name="todo_delete"),
]
