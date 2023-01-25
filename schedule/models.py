from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField(auto_created=True)
    deadline = models.DateTimeField()
    marks = models.BooleanField(default=False)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        ordering = ["marks", "-create_date"]

    def __str__(self):
        return f"{self.content} {self.marks} {self.tags}"
