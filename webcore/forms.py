from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import media, webpage,website,text_block,contents
from cloudinary.forms import CloudinaryFileField

class websiteForm(forms.ModelForm):
    class Meta:
        model= website
        fields = ('hname',)

class picForm(forms.ModelForm):
    class Meta:
        model = text_block
        fields= ('cont',)

#class txtForm(forms.ModelForm):
 #   class Meta:
  #      model= text_block
   #     fields = ('text','cont',)


class txtForm(forms.ModelForm):
    class Meta:
        model = text_block
        fields=('cont','text')

class save_mediaform(forms.ModelForm):
    class Meta:
        model= media
        fields=('med',)