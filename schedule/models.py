from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Tag name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(blank=True, verbose_name="Content")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Create date")
    deadline = models.DateTimeField(auto_now=False, null=True, blank=True, verbose_name="Deadline")
    is_mark = models.BooleanField(default=False, verbose_name="Execution mark")
    tags = models.ManyToManyField(Tag, blank=True, default=None, related_name="tasks")

    class Meta:
        ordering = ["is_mark", "-create_date"]

    def __str__(self):
        return f"{self.content} {self.is_mark} {self.tags}"
