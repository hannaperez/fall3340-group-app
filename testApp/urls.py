from django.urls import path, include 
from . import views #within the same directory(.) import views  

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name = 'home'), 
]
