from django.contrib import admin
from .models import Task, Username

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Task

class UsernameAdmin(admin.ModelAdmin):
    class Meta:
        model = Username

admin.site.register(Task, MyModelAdmin)
admin.site.register(Username, UsernameAdmin)
