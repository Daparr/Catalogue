import uuid

from django.db import models

from catalogue import settings


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='images/', default=None)
    id = models.AutoField(primary_key=True, editable=False)

# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)