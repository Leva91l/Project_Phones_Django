from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateField()
    
    def __str__(self):
        return self.name