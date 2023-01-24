from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from schedule.models import Task, Tag


@login_required
def index(request):
    """View function for the home page of the site."""

    context = {
        "todo_list": Task.objects.all(),
        "tags": Tag.objects.all()
    }

    return render(request, "schedule/index.html", context=context)


class TaskCreateView(generic.CreateView):
    pass


class TagCreateView(generic.CreateView):
    pass


class TagUpdateView(generic.UpdateView):
    pass


class TagDeleteView(generic.DeleteView):
    pass
