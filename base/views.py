from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


rooms=[
    {'id':1, 'name':"Romm no 1 for ifykwyk"},
    {'id':2, 'name':'Only Studies'},
    {'id':3, 'name':'Keep studyn biches'},
]
# room template
# we have pk ahic is passedinto function by ui and another list in db
# if pk matches id of db thenreturn pk objkect into room.html
def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i

    context={'room':room}
    return render(request,'base/room.html',context)