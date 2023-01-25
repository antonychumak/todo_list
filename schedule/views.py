from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from schedule.models import Task, Tag


@login_required
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


class TaskCreateView(generic.CreateView):
    pass


class TaskUpdateView(generic.UpdateView):
    pass


class TaskDeleteView(generic.DeleteView):
    pass


class TagCreateView(generic.CreateView):
    pass


class TagUpdateView(generic.UpdateView):
    pass


class TagDeleteView(generic.DeleteView):
    pass

