
from django.urls import path
from .views import register,signin,profile
urlpatterns = [
 path('register/', register,name='register'),
 path('signin/',signin,name='signin'),
 path('profile/',profile,name='profile')
]