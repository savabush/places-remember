from django import forms
from .models import Memory


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'floatingName', 'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'id': 'floatingDesc', 'class': 'form-control'})
        }