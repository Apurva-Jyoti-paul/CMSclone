from django.contrib import admin
from .models import website,webpage,text_block

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

admin.site.register(website)
admin.site.register(webpage,webpageAdmin)
admin.site.register(text_block)


# Register your models here.

