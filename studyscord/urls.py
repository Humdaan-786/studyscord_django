from django.contrib import admin
from django.urls import path,include

# http stuff
# from django.http import HttpResponse

# #define dunction to render after matching path

# def home(request):
#     return HttpResponse('<h1>Home page bitches</h1>')

# here if the url path is an empty string it is redirected into base.urls taht is anothe app
# so we are following good practice and seperting routing of components from main app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),

    # path('', home),

]
