from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Address(models.Model):
    city=models.CharField(max_length=15)
    postal_code=models.IntegerField()
    street_no=models.IntegerField()

    

   

class chef(models.Model):
    first_name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.ForeignKey(Address, on_delete=models.CASCADE,null=True)


class Dishes(models.Model):
    dish_name=models.CharField(max_length=40)
    price=models.IntegerField()
    rating=models.IntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(10)
    ])
    chef=models.ForeignKey(chef, on_delete=models.CASCADE,null=True)
   
    