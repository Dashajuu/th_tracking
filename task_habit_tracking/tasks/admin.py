from django.contrib import admin

from .models import Task, Category, Status

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Status)
