from . import views
from django.urls import path

urlpatterns=[
    path('home/',views.index,name='home'),
    path('view/<key>',views.view,name='view'),
]