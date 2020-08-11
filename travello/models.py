from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(default='')
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)