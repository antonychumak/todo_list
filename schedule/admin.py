from django.contrib import admin

from schedule.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display
    search_fields = ("deadline",)
    prepopulated_fields = {"slug": ("tags",)}
