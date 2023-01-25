from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Tag name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Task(models.Model):
    content = models.TextField(blank=True, verbose_name="Content")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Create date")
    deadline = models.DateTimeField(auto_now=False, verbose_name="Deadline")
    marks = models.BooleanField(default=False, verbose_name="Execution mark")
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Tag name")

    # def get_absolute_url(self):
    #     return reverse("taxi:driver-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.content} {self.marks} {self.tags}"

    class Meta:
        ordering = ["marks", "-create_date"]


