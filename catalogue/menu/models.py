from django.db import models


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=255, default=None)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='images/', default=None)
    id = models.PositiveIntegerField(primary_key=True)