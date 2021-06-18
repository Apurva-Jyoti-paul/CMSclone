from django import forms
from django.forms import fields, models
from django.forms.forms import Form
from .models import media, testtext, webpage,website,text_block,contents
from cloudinary.forms import CloudinaryFileField

from ckeditor.fields import RichTextField


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
        fields=('med','resourcetype',)

class save_contents(forms.ModelForm):
    class Meta:
        model= contents
        fields=('text','align',)

class pageForm(forms.ModelForm):
    class Meta:
        model= webpage
        fields=('title','identifier',)

class testform(forms.ModelForm):
    text=RichTextField()
    class Meta:
        model=testtext
        fields=('title','text')