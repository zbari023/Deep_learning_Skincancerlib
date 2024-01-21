from django import forms  # load the forms-bibliothek from django
from .models import UserData , Prediction, Contact  # load the classes from the model




class NameuploadForm(forms.ModelForm):   # This form-class is responsible to get the data from the user like name,email and phone
    class Meta:
        model = UserData
        fields = ['name','email','telefonnummer']


class ContactForm(forms.ModelForm):  # This form-class is responsible to get the data from the user, when he send his data in message type in html-area
    class Meta:
        model = Contact
        fields = '__all__'