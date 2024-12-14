from django.urls import path
from . import views
#define dunction to render after matching path
# <str:pk> denotes taht detect chnages in url and redirects them to views then views cretes 
# and renders templates for them according to pk passsed in url
urlpatterns=[
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
]
