from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Room 
# Create your views here.
from .forms import RoomForm

#coding logic page for allactions being taken on website


def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


# rooms=[
#     {'id':1, 'name':"Romm no 1 for......"},
#     {'id':2, 'name':'Only Studies'},
#     {'id':3, 'name':'Keep studyin...'},
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
    # empty obj or empty row of Room table 
    form = RoomForm()
    # this objs attributes will be filled by page's input fields
    # Now when post api call is being made form's POST method next lines are being 
    # executed
    if request.method == "POST":
        print(request.POST)
        # we got a dic of key list of values assosiated with it
        # filling or form obj with that dictionaries values
        form = RoomForm(request.POST)
        if form.is_valid():
            # check if valid GOOD Coding Practice
            form.save()
            # save to db and redirect
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)

# form view
def updateRoom(request,pk):
    # selection of alredy filled row of table
    room  = Room.objects.get(id=pk)
    # slection of values filled in form
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