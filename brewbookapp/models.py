from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Drink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_drinks', null=True)
    name = models.CharField(max_length=100)
    instruction = models.TextField()
    photo = models.ImageField(upload_to='media/photos', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video = models.FileField(upload_to='media/videos', blank=True, null=True)
    fun_facts = models.TextField(blank=True, null=True)

class Ingredient(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=100)

class Liked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='liked_drinks')
    