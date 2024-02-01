from django.db import models

# Create your models here.

# Models class for the Admin Infomations
class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=25, null=True , blank=True)
    email_us = models.CharField(max_length=25, null=True , blank=True)
    subtitle = models.TextField(max_length=200, null=True , blank=True)
    email = models.TextField(max_length=200, null=True , blank=True)
    phones = models.TextField(max_length=200, null=True , blank=True)
    address = models.TextField(max_length=200, null=True , blank=True)
    fb_link = models.URLField(null=True , blank=True)
    insta_link = models.URLField(null=True , blank=True)
    tiktok_link = models.URLField(null=True , blank=True)
    youtube_link = models.URLField(null=True , blank=True)
    android_store = models.URLField(null=True , blank=True)
    apple_store = models.URLField(null=True , blank=True)
    
    def __str__(self):
        return self.name

class UserData(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefonnummer = models.CharField(max_length=40)
    def __str__(self):
        return self.name 

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email


# Models class for the uploaded image from User with the prediction result of Image  
class Prediction(models.Model): # hier is a django model class, which the inheritance is from 'models.Model'
    image = models.ImageField(upload_to='skinlib/') # for saving the image in media-file in the project
    predicted_class = models.CharField(max_length=255) # for the prediction skin cancer label
    confidence = models.FloatField() # for the percent of the prediction-image

    def __str__(self):
        return f"{self.predicted_class} - {self.confidence}%" # that will be display in Django-Administration-site 