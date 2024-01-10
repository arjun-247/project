from django.db import models

# Create your models here.
class Shoes(models.Model):
    brand=models.CharField(max_length=250)
    gender=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    sale=models.CharField(max_length=10)
    image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
    