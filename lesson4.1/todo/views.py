from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.urls import reverse
from todo.forms import TodoForm

from todo.models import Todo

# Create your views here.

User = get_user_model()

def homeview(request):
    title = "todo"

    todos = Todo.objects.all()
    context = {"title": title, "todos":todos}
    return render(request, "todo/index.html", context)


def todocreateview(request):
    page_title = "todo"

    if request.method == "POST": 
        title = request.POST["title"]
        description = request.POST["description"]
        date = request.POST["date"]
        time = request.POST["time"]

        user = request.POST["user"]

        author = User.objects.get(id=user)

        Todo.objects.create(
            title = title,
            description = description,
            date = date,
            time = time,
            user = author,
        )

        return redirect(reverse("home")) 
    
    users = User.objects.all()

    context = {"users":users, "title":page_title}

    return render(request, "todo/todo_create.html", context)

def tododetailview(request, id):
    page_title = "todo"

    context = {}

    obj = get_object_or_404(Todo, id = id)

    context["object"] = obj
    context["title"] = page_title

    return render(request, "todo/todo_detail.html", context)

def todoupdateview(request, id):
    page_title = "todo"

    context = {}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Todo, id = id)
 
    # pass the object as instance in form
    form = TodoForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect(reverse("todo_detail", kwargs={'id': id})) 
 
    # add form dictionary to context
    context["form"] = form
    context["title"] = page_title

    return render(request, "todo/todo_update.html", context)

def tododeleteview(request, id):
    page_title = "todo"

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Todo, id = id)

    if request.method == "POST":
        obj.delete()

        return redirect(reverse("home"))
    
    context["title"] = page_title

    return render(request, "todo/todo_delete.html", context)
    