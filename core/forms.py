from django.forms import ModelForm
from .models import Memory


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'comment']
