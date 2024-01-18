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
            imgform.save()
            return redirect('/')
    else:
        imgform = ImageUploadForm()
    return render(request,'skinlib/index.html',{'imgform': imgform})
