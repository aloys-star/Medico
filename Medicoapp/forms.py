from django import forms
from Medicoapp.models import appointment,ImageModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields =['name','email','phone','department','date','doctor','message']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields =['image','title','price']