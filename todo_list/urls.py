from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from todo_list.views import (
    HomeView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TagListView,
    ToggleDoneView
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
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path('tasks/<int:pk>/toggle_done/', ToggleDoneView.as_view(), name='toggle-done'),

    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete")
]

app_name = "todo_list"
