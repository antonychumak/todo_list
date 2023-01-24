from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    create_date = models.DateField(auto_created=True)
    deadline = models.DateField(auto_now_add=True)
    marks = models.BooleanField()
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        ordering = ["create_date", "-marks"]

    def __str__(self):
        return f"{self.content} {self.marks}"
