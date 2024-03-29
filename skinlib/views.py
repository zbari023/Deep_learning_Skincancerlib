# Hier werden alle benötigten Bibliotheken und Module importiert.
# Darunter sind Django-spezifische, Modelle, Formulare, Dateispeicherung, TensorFlow-Funktionen usw.

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import NameuploadForm ,ContactForm
from .models import  UserData ,Contact, Prediction
from django.core.files.storage import FileSystemStorage
# Tensorflow-Bibliothek muss in der virtuelles Umgebebung mit dem Befehl 'pip install tensorflow' installiert
from tensorflow.keras.preprocessing.image import load_img, img_to_array 
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.models import load_model
import os
import numpy as np
from pathlib import Path
# Create your views here.

# Definieren des CNN_Modellpfads. skinlib-CNN-Modells wird in der src/cnnmodell gespeichert.
BASE_DIR = Path(settings.BASE_DIR)
MODEL_PATH = str(BASE_DIR / 'cnnmodell' / 'skin_cancer_model_multible_classifier.h5')
# Definieren  der Hautkrebsklassennamen
CLASS_NAMES = [
    'Actinic keratosis', 'Basal cell carcinoma', 'Benign keratosis', 'Dermatofibroma',
    'Melanocytic nevus', 'Melanoma', 'Squamous cell carcinoma', 'Vascular lesion'
]

# Laden des CNN-Modells
CUSTOM_MODEL = load_model(MODEL_PATH)
# predict-Funktion wird aufgerufen, wenn ein Benutzer eine Vorhersage für sein hochgeladenes Hautbild machen möchte.

def predict(request):
    if request.method == 'POST' and 'imagefile' in request.FILES:
        try:
            # Hochgeladenes Bild wird erhalten und gespeichert
            imagefile = request.FILES['imagefile']
            fs = FileSystemStorage()
            filename = fs.save(os.path.join(settings.MEDIA_ROOT, 'images', imagefile.name), imagefile)
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', imagefile.name)
            # Bild wird geladen und vorverarbeitet, um es für das Modell vorzubereiten
            target_size = (64, 64)
            image = load_img(image_path, target_size=target_size)
            image = img_to_array(image)
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            image = preprocess_input(image)
            # Vorhersage mit dem geladenen Modell wird durchgeführt
            predictions = CUSTOM_MODEL.predict(image)
            class_probabilities = predictions[0]
            class_index = np.argmax(class_probabilities)
            predicted_class_name = CLASS_NAMES[class_index]
            # Die Vorhersage wird in der Datenbank gespeichert
            prediction_obj = Prediction(
                image=imagefile,
                predicted_class=predicted_class_name,
                confidence=class_probabilities[class_index] * 100
            )
            prediction_obj.save()
            # Das Ergebnis wird dem Benutzer angezeigt
            return render(request, 'skinlib/predict.html', {'prediction_obj': prediction_obj})
        except Exception as e:
            # Fehlerbehandlung, falls ein Fehler auftritt
            return render(request, 'skinlib/predict.html', {'error': f'Error processing image: {str(e)}'})
    return render(request, 'skinlib/predict.html', {'error': 'No file part'})



def home(request):
    images = Prediction.objects.all().count()  # given the counter of the images in the project
    user = UserData.objects.all().count()      # given the counter of the users in the project
    contacting = Contact.objects.all().count() # given the counter of the contacting in the project
    if Prediction.objects.exists():            # to display just the current image in html
        image = Prediction.objects.latest('id')
        context = {'image': image}
    else:
        context = {'image': None}
    
    if request.method == 'POST':
        form = NameuploadForm(request.POST)    # gitting the request data from the form-class, which content the userdata
        eform = ContactForm(request.POST)      # gitting the request data from the form-class, which content the contact data
        if form.is_valid():
            form.save()                        # saving the request data in db
            return redirect('answeruser/')     # Redirect to a page to make sure for the user, that his image is uploaded
        if eform.is_valid(): 
            eform.save()
            return redirect('answermessage/')  
    else:
        form = NameuploadForm()
        eform = ContactForm()
    # sending the data with the context proccessor to html 
    context.update({'form': form,'eform': eform,'images':images ,'user': user ,'contacting': contacting })
    return render(request, 'skinlib/index.html', context)





# make the dashboard function data 
def dashboard(request):
    images = Prediction.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'skinlib/dashboard.html',{
        'images':images ,                 # some context data, that used in django-html
        'user': user , 
        'contacting': contacting 
    })
    
# create the answer page for making sure, that the user his data is uploaded
def answeruser(request):
    images = Prediction.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'skinlib/answeruser.html',{
        'images':images , 
        'user': user , 
        'contacting': contacting 
    })
    
# create the answer page for making sure, that the user his data is uploaded
def answerimg(request):
    images = Prediction.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'skinlib/answerimg.html',{
        'images':images , 
        'user': user , 
        'contacting': contacting 
    })
# create the answer page for making sure, that the user his data is uploaded
def answermessage(request):
    images = Prediction.objects.all().count()
    user = UserData.objects.all().count()
    contacting = Contact.objects.all().count()
    return render(request,'skinlib/answermessage.html',{
        'images':images , 
        'user': user , 
        'contacting': contacting 
    })
    










""" def home(request):
    if request.method == 'POST':
        imgform = ImageUploadForm(request.POST, request.FILES)
        if imgform.is_valid():
            imgform.save()
            return redirect('/')
    else:
        imgform = ImageUploadForm()
    return render(request,'skinlib/index.html',{'imgform': imgform})
 """