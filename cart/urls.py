
from django.urls import path
from .views import cart,add_to_cart,remove_cart_item,remove_cart
urlpatterns = [
 path('', cart,name='cart'),
 path('<int:product_id>/',add_to_cart,name='add_to_cart'),
 path('remove/<int:product_id>/', remove_cart_item, name='remove_cart_item'),
 path('delete/<int:product_id>/', remove_cart, name='remove_cart'),
]