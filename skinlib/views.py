from django.shortcuts import render, redirect
from django.conf import settings
from .models import Image
from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.models import load_model
import os
import numpy as np
from pathlib import Path
# Create your views here.

# Define constants
BASE_DIR = Path(settings.BASE_DIR)
MODEL_PATH = str(BASE_DIR / 'cnnmodell' / 'skin_cancer_model_multible_classifier.h5')
CLASS_NAMES = [
    'Actinic keratosis', 'Basal cell carcinoma', 'Benign keratosis', 'Dermatofibroma',
    'Melanocytic nevus', 'Melanoma', 'Squamous cell carcinoma', 'Vascular lesion'
]

# Load the model outside of the view function
CUSTOM_MODEL = load_model(MODEL_PATH)




def home(request):
    if request.method == 'POST':
        imgform = ImageUploadForm(request.POST, request.FILES)
        if imgform.is_valid():
            image = imgform.save(commit=False)  # Save the form object without committing to the database yet
            image.save()  # Save the image object to the database
            imagefile = image.image

            try:
                fs = FileSystemStorage()
                filename = fs.save(os.path.join(settings.MEDIA_ROOT, 'images', imagefile.name), imagefile)

                image_path = os.path.join(settings.MEDIA_ROOT, 'images', imagefile.name)

                target_size = (64, 64)
                image = load_img(image_path, target_size=target_size)
                image = img_to_array(image)
                image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
                image = preprocess_input(image)

                predictions = CUSTOM_MODEL.predict(image)
                class_probabilities = predictions[0]
                class_index = np.argmax(class_probabilities)

                predicted_class_name = CLASS_NAMES[class_index]



                classification_result = {
                    'class': predicted_class_name,
                    'confidence': class_probabilities[class_index] * 100
                }

                return render(request, 'skinlib/index.html', {'classification_result': classification_result})

            except Exception as e:
                # Provide a more detailed error message
                return render(request, 'skinlib/index.html', {'error': f'Error processing image: {str(e)}'})
    else:
        imgform = ImageUploadForm()
    
    return render(request, 'skinlib/index.html', {'imgform': imgform})
















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