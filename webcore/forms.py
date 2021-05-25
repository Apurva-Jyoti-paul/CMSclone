from django import forms
from .models import webpage,website,text_block

class websiteForm(forms.ModelForm):
    class Meta:
        model= website
        fields = ('hname',)
