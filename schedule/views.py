from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import CreateView, UpdateView, DeleteView

from schedule.models import Task, Tag


def index(request):
    context = {
        "todo_list": Task.objects.all(),
    }

    return render(request, "schedule/index.html", context=context)


def tags_list_view(request):
    context = {
        "tags": Tag.objects.all(),
    }

    return render(request, "schedule/tags.html", context=context)


class MarkUpdateView(View):
    def post(self, request, slug):
        task = Task.objects.get(slug=slug)
        task.is_mark = not task.is_mark
        task.save()
        return redirect("schedule:index")

    def get(self, request, **kwargs):
        return redirect("schedule:index")


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("schedule:index")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("schedule:index")


class TaskDeleteView(DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("schedule:index")


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("schedule:tags")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("schedule:tags")


class TagDeleteView(DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("schedule:tags")
