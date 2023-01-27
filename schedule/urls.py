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
    path(
        "tags/create",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<slug:slug>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<slug:slug>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "tasks/create",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<slug:slug>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<slug:slug>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
]

app_name = "schedule"
