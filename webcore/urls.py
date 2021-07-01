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
    path('activity/',views.show_all,name='activity'),
    path('delete/<key>',views.delete_website,name="delete"),
    path('objectinfo/<key>',views.action_panel,name='objectinfo'),
    path('',views.base,name='base'),
    path('testalpha/<key>/<optional>',views.take_test,name='testwrite'),
    path('testbeta/<key>/<key2>',views.show_testt,name='testread'),
    path('delpag/<key>/<k>',views.delete_text,name='delpag'),
    path('modify/<key>/<k>',views.modify_test,name='modify'),
    path('publish/<key>/<key2>',views.change_visibilty,name='publish'),
]

