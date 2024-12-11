from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Room 
# Create your views here.
from .forms import RoomForm


def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


# rooms=[
#     {'id':1, 'name':"Romm no 1 for ifykwyk"},
#     {'id':2, 'name':'Only Studies'},
#     {'id':3, 'name':'Keep studyn biches'},
# ]
# room template
# we have pk ahic is passedinto function by ui and another list in db
# if pk matches id of db thenreturn pk objkect into room.html
def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)

# form view
def createRoom(request):
    form=RoomForm()
    if request.method == "POST":
        print(request.POST)
        # we got a dic of key list of values assosiated with it
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'base/room_form.html',context)

# form view
def updateRoom(request,pk):
    room  = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    # we ahve selected a single row of room table by mathcing pk or id
    if request.method == "POST":
        form=RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)    

def deleteRoom(request,pk):
    room  = Room.objects.get(id=pk)

    # we ahve selected a single row of room table by mathcing pk or id
    if request.method == "POST":
        room.delete()
        return(redirect('home'))
    return render(request,'base/delete.html',{'obj':room})    