from django.urls import path

from .views import (
    index,
    tags_list_view,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", tags_list_view, name="tags"),
    path("tags/create", TagCreateView.as_view, name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view, name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view, name="tag-delete"),
    path("tasks/create", TaskCreateView.as_view, name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view, name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view, name="task-delete"),
    ]

app_name = "schedule"
