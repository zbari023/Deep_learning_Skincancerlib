from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageUploadForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        imgform = ImageUploadForm(request.POST, request.FILES)
        if imgform.is_valid():
            imgform.save()
            return redirect('/')
    else:
        imgform = ImageUploadForm()
    return render(request,'skinlib/index.html',{'imgform': imgform})
