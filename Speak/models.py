from django.db import models

# Create your models here.
class Speak(models.Model):
    content = models.TextField(blank = True)
