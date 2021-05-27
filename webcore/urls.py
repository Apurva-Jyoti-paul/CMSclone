from . import views
from django.urls import path

urlpatterns=[
    path('home/',views.index,name='home'),
    path('view/<key>',views.view,name='view'),
    path('Createwebsite/',views.create_website,name='create-website'),
    path('betaform/<key>/<k>',views.betaformview,name='betaview'),
    path('editbeta/<key>',views.edit_pagetxt,name='betaedit'),
]