from django.contrib import admin

# Register your models here.
from .models import Task, Category, Priority, SubTask, Note

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(SubTask)
admin.site.register(Note)