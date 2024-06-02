from django import forms
from .models import Speak

class SpeakForm(forms.ModelForm):
    content = forms.CharField(required=False,
     widget = forms.Textarea(
        attrs={
            "placeholder": "What you got?"
        }
     )
    )

    link_to_access = forms.URLField(required=False,
     widget = forms.URLInput(
        attrs={
            "placeholder": "Enter url",
            "class": "link-input",           
        }
     )
    )

    img = forms.ImageField(required=False,
                           )
    
    class Meta:
        model = Speak
        fields = [
            'content',
            'link_to_access',
            'img',
            'language',
        ]
    