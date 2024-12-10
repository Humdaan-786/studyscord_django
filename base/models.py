from django.db import models

from django.contrib.auth.models  import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# a topic can have multiple rooms whereas a room canhave only one
# topic

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    # return data type of this class
    # this piece of code returns the name field of isinstance
    # or name of room in string format

    
    # here Date time is used for saving timestamps
    # auto_now truew updates on every save and add one 
    # takes timestamps only once at creatiion

# second model Messaeg this is a one to maney realtionship
# one to maney because one room will post multiple messages

class Message(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    # room = 
    # cascade is when a room is deletd all meesages will be deletd
    # defining raltion with model table
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.body[0:50]
    

