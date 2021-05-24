from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

al= (
    ('center','center'),
    ('left','left'),
    ('right','right')
)

class website(models.Model):
    
    hname= models.CharField(max_length=1000)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)



class webpage(models.Model):

    web = models.ForeignKey(website,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default='untitled')
    update = models.DateTimeField(auto_now=True)
    identifier = models.CharField(max_length=1000,primary_key=True)

class text_block(models.Model):

    page = models.ForeignKey(webpage,on_delete=models.CASCADE)
    seq = models.IntegerField(default=0)
    align= models.CharField(max_length=10,default='center',choices=al)
    text = models.CharField(blank=True,max_length=10000,null=True)
    cont = CloudinaryField('media',null=True,blank=True)
        



# Create your models here.
