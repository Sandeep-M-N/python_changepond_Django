from django.db import models

# Create your models here.
class Dishes(models.Model):
    dish_name=models.CharField(max_length=50)
    price=models.IntegerField()
    