from django.shortcuts import render
from .models import Speak
from .forms import SpeakForm
from gtts import gTTS


def text_create_view(request):
    form = SpeakForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SpeakForm()
    context = {"form":form}
    return render(request, "Speak/create.html",context)



