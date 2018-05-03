from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
