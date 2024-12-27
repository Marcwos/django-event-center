from django import forms
from .models import Service
from cloudinary.forms import CloudinaryFileField
from .models import Photo


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']


class PhotoForm(forms.ModelForm):
    image= CloudinaryFileField()
    
    class Meta:
        model = Photo 
        fields= ['title','image']
