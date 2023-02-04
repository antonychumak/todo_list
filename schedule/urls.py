from django.urls import path

from .views import (
    index,
    tags_list_view,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    MarkUpdateView
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", tags_list_view, name="tags"),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tag/<slug:slug>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<slug:slug>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "tasks/create/",
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
    path(
        "tasks/<slug:slug>/mark/",
        MarkUpdateView.as_view(),
        name="task-change"
    )
]

app_name = "schedule"
