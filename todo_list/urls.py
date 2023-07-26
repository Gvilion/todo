from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from todo_list.views import (
    HomeView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView
)

urlpatterns = [
    path(
        "",
        RedirectView.as_view(
            url=reverse_lazy("todo_list:home")
        )
    ),
    path("task/", HomeView.as_view(), name="home"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete")
]

app_name = "todo_list"
