from django.shortcuts import render, redirect
from .models import Speak
from .forms import SpeakForm
from gtts import gTTS
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from deep_translator import GoogleTranslator

def text_create_view(request):
    if request.method == 'POST':
        form = SpeakForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('content-speak')
    else:
        form = SpeakForm()

    context = {"form": form}
    return render(request, "Speak/create.html", context)

def web_scrape():
    page = requests.get(Speak.objects.last().link_to_access)
    soup  = BeautifulSoup(page.text, "html.parser")
    heading = soup.find('h1')
    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraphs])
    main_content = 'Title : ' + heading.get_text() + " ." + " ".join(content.split())
    return main_content

def audio_output_view(request):   
    #import pythoncom
    #pythoncom.CoInitialize()
    # Retrieve the last saved text from the model (or use any other logic to get the desired text)
    
    if Speak.objects.last().content:
        last_saved_text = Speak.objects.last().content

    elif Speak.objects.last().link_to_access:
        last_saved_text= web_scrape()
        
    else:
        image_path = Speak.objects.last().img.path
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        last_saved_text = text
    
    language = Speak.objects.last().language
    translated_text = GoogleTranslator(source='auto', target=language).translate(last_saved_text)
    tts = gTTS(text = translated_text[:1000], lang = language)

    # Save the speech output as a temporary file
    temp_audio_file = "/Users/jalaj/Desktop/V/Lingual/Static/temp_audio.mp3"
    tts.save(temp_audio_file)
    context = {'object':translated_text,
        'audio_url': '/static/temp_audio.mp3'}
    return render(request, 'Speak/content.html', context) 