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

def audio_output_view(request):
    #import pythoncom
    #pythoncom.CoInitialize()
    # Retrieve the last saved text from the model (or use any other logic to get the desired text)
    last_saved_text = Speak.objects.last().content  
    tts = gTTS(text = last_saved_text, lang='en')
    # Save the speech output as a temporary file
    temp_audio_file = "C:\\Users\\hp\\Desktop\\harshit\\dev\\project_assistant\\Lingual\\Static\\temp_audio.mp3"
    tts.save(temp_audio_file)
    context = {'object':last_saved_text,
        'audio_url': '/static/temp_audio.mp3'}
    return render(request, 'Speak/content.html', context)
