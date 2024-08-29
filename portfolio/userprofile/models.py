from django.db import models
from django.utils.text import slugify
# Create your models here.
class Tags(models.Model):
    caption = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.caption}"
class Author(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email_address = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name}"
class Portfolio(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    posted_by=models.DateField()
    slug=models.SlugField(default='',db_index=True,editable=False)
    author  = models.ForeignKey(Author,on_delete=models.CASCADE) 
    tags = models.ManyToManyField(Tags)
    def save(self, *args, **kwargs):
      
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
    
class feedback(models.Model):
    full_name=models.CharField(max_length=20)
    email=models.EmailField()
    description=models.TextField()
    post = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name}"
