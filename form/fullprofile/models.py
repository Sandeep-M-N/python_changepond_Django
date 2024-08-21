from django.db import models

# Create your models here.
class Profileupload(models.Model):
    # userimage=models.FileField(upload_to='images')
    userimage=models.ImageField(upload_to='images')
    #to use imagefield we need to install pillow
    #i.e pip install pillow