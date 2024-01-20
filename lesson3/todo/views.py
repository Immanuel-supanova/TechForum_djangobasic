from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo
# Create your views here.

def home(request):
    title = "Todo"
    context = {"title":title}
    return render(request, "todo/index.html", context)
