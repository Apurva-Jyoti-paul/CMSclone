from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


al= (
    ('center','center'),
    ('left','left'),
    ('right','right')
)

class website(models.Model):
    
    hname= models.CharField(max_length=1000)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.hname


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
    link = models.URLField(max_length=1000,null=True)

        

class contents(models.Model):

    pag = models.ForeignKey(webpage,on_delete=models.CASCADE)
    text= models.CharField(max_length=10000)
    text2=models.CharField(max_length=100,null=True)
    align= models.CharField(max_length=50,null=True,default="left")
    dc=models.CharField(max_length=20,null=True)
    
class media(models.Model):
    med = models.URLField(max_length=1000,null=True)
    webp= models.ForeignKey(webpage,on_delete=models.CASCADE)
    resourcetype= models.CharField(max_length=10,null=True)

class testtext(models.Model):
    title=models.CharField(max_length=1000,default='untitled')
    text=RichTextField()
    visibility=models.IntegerField(default=1)
    site=models.ForeignKey(website,on_delete=models.CASCADE,default=7)
    time=models.DateTimeField(null=True,auto_now_add=True)
    text2=RichTextUploadingField(blank=True,null=True,external_plugin_resources=[(
        'youtube',
        '/static/webcore/youtube/',
        'plugin.js',
    )],
    )
# Create your models here.my
