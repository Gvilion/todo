from django.shortcuts import render
from django.views import generic

from todo_list.models import Task


class HomeView(generic.ListView):
    model = Task
    paginate_by = 5

