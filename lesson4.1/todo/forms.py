from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'description':forms.Textarea(attrs={"class":"form-control"}),
            'date':forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            'time':forms.TimeInput(attrs={"class":"form-control", "type":"time"}),
            'user':forms.Select(attrs={"class":"form-select"}),
        }
