
from django.urls import path
from .views import completedOrder
urlpatterns = [
 path('', completedOrder,name='order_complete'),
]