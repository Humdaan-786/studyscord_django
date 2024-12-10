from django.db import models

# Create your models here.
class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    # this piece of code returns the name field of isinstance
    # or name of room in string format

    
    # here Date time is used for saving timestamps
    # auto_now truew updates on every save and add one 
    # takes timestamps only once at creatiion