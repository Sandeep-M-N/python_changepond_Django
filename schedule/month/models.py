from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(35)]) # validators
    city=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.first_name} and {self.last_name}'