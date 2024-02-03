from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from todo.forms import TodoForm

from todo.models import Todo

from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView


User = get_user_model()


class HomeView(TemplateView):
    """"""
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        title = "todo"
        context['todos'] = Todo.objects.all()
        context['title'] = title
        return context
    

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo_create.html'
    form_class = TodoForm

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        title = "todo"
        context['title'] = title
        return context


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/todo_detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        title = "todo"
        context['title'] = title
        return context


class TodoUpdateView(UpdateView):
    template_name = "todo/todo_update.html"
    form_class = TodoForm
    model = Todo

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        title = "todo"
        context['title'] = title
        return context
    

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/todo_delete.html"

    def get_success_url(self) -> str:
        return reverse("home")

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        title = "todo"
        context['title'] = title
        return context
