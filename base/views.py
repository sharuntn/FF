from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from base.forms import ImageForm
from .mingo import *
from PIL import Image
from django.core.files.storage import FileSystemStorage

#from mingo import *
# Create your views here.
def loginPage(request):
    return render(request,'base/login.html')

def rgPage(request):
     return render(request,'base/register.html')

def homePage(request):
    return render(request,'base/index.html')
def scan(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

            return render(request,'base/scan.html',{'form':form,'img_obj':img_obj})
    else:
        form = ImageForm()
        return render(request,'base/scan.html', {'form': form})
    
    
def result(request):
    print(request.POST)
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                img_obj = form.instance
                value = prediction(img_obj.image)
                
        return render(request,'base/result.html',{'form':form,'img_obj':img_obj,'value':value})
   

