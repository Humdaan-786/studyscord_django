from django.forms import ModelForm
from .models import Room

# predefined dj form for rendering all fields of available db
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields ='__all__'
