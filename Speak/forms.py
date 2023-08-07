from django import forms
from .models import Speak

class SpeakForm(forms.ModelForm):
    content = forms.CharField(required=False,
     widget = forms.Textarea(
        attrs={
            "placeholder": "Description",
            "class":"new-class-name-two",
            "rows":10,
            "cols":50,
        }
     )
    )
    class Meta:
        model = Speak
        fields = [
            'content'
        ]
    