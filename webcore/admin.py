from webcore.forms import testform
from django.contrib import admin
from django.contrib.admin.sites import site
from .models import contents, media, testtext, viewip, website,webpage,text_block

class webpageInline(admin.StackedInline):

    model= webpage
    extra = 1

class text_blockInline(admin.StackedInline):
    model = text_block
    extra = 2



class webpageAdmin(admin.ModelAdmin):
    model=webpage
    fields= ['web','title','identifier']
    inlines=[text_blockInline]

admin.site.register(contents)
admin.site.register(media)
admin.site.register(website)
admin.site.register(webpage,webpageAdmin)
admin.site.register(text_block)
admin.site.register(testtext)
admin.site.register(viewip)
# Register your models here.

