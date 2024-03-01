from django import forms
from .models import Speak

class SpeakForm(forms.ModelForm):
    content = forms.CharField(required=False,
     widget = forms.Textarea(
        attrs={
            "placeholder": "What you got?",
            "class": "form-con",
        }
     )
    )
    class Meta:
        model = Speak
        fields = [
            'content'
        ]
    