from django import forms  # load the forms-bibliothek from django
from .models import Image



class ImageUploadForm(forms.ModelForm): # This form-class is responsible to get the data from the image in html page
    class Meta:
        model = Image
        fields = ['image','result']
