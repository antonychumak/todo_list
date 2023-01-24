from django.urls import path

from .views import (
    index,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/create", TaskCreateView.as_view, name="task-create"),
    path("tags/create", TagCreateView.as_view, name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view, name="tag-update"),
    path("tasks/<int:pk>/delete/", TagDeleteView.as_view, name="task-delete"),
    ]

app_name = "schedule"
