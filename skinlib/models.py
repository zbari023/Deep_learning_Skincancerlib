from django.db import models

# Create your models here.


# Models class for the uploaded image with his result
class Image(models.Model):
    image = models.ImageField(upload_to='skinlib')
    result = models.CharField(max_length=100)
    def __str__(self):
        return self.image.name