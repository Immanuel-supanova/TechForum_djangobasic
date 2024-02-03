from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'description':forms.Textarea(attrs={"class":"form-control"}),
            'deadline':forms.DateTimeInput(attrs={"class":"form-control"}),
            'user':forms.Select(attrs={"class":"form-select"}),
        }
