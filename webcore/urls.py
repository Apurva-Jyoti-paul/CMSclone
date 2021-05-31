from . import views
from django.urls import path

urlpatterns=[
    path('home/',views.index,name='home'),
    path('view/<key>',views.view,name='view'),
    path('Createwebsite/',views.create_website,name='create-website'),
    path('betaform/<key>/<k>',views.betaformview,name='betaview'),
    path('editbeta/<key>',views.edit_pagetxt,name='betaedit'),
    path('mediasave/<key>/<k>',views.save_media,name='savemedia'),
    path('savecontent/<k>/<key>',views.save_content,name='savecontent'),
    path('watch/<key>/<k>',views.watch,name='watch'),
    path('newpage/<key>',views.crt_page,name='createpage'),
]