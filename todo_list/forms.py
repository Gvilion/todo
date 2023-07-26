from django import forms

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["content", "tags", "deadline"]
        widgets = {
            "deadline": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "datetime-local"
                }
            ),
        }
