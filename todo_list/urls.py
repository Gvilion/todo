from django.urls import path

from todo_list.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]

app_name = "todo_list"
