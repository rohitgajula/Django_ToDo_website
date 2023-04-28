from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task                    # model we are trying to create form.
        fields = '__all__'              # what fields that we are gonna allow in that form.

        