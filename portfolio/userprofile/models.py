from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=600)
    date=models.DateField()
    time=models.TimeField()
    posted_by=models.DateField()

    def __str__(self):
        return f"{self.title}"