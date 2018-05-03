from django.contrib import admin
from .models import Task

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Task

admin.site.register(Task, MyModelAdmin)
