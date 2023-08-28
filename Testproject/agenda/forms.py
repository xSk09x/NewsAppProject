from .models import Narrative
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class NarrativeForm(ModelForm):
    class Meta:
        model = Narrative
        fields = ['name', 'intro', 'full_text', 'datentime']
        widgets = {
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Narrative name'
            }),
        
            'intro' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Narrative intro'
            }),

            'full_text' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Narrative text'
            }),

            'datentime' : DateTimeInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Narrative date and time'
            })
        }
