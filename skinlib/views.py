from django.shortcuts import render
from .models import Image
# Create your views here.


def home(request):
    data = Image.objects.all()
    return render(request,'skinlib/index.html',{'data':data})

