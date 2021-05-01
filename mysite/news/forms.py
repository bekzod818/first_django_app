from django.forms import ModelForm, TextInput, Textarea
from .models import Tutorial

class TutorialForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = [
            'title',
            'content',
            # 'create'
        ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sarlavha nomi'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Maqola nomi'
            })
        }
