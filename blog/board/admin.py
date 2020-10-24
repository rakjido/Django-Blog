from django.contrib import admin

from .models import Board


@admin.register(Board)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author")
