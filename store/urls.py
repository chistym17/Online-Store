
from django.urls import path
from .views import store,product_detail
urlpatterns = [
 path('store/', store,name='store'),
 path('store/category/<slug:category_slug>/', store,name='filter_products'),
 path('<slug:category_slug>/<slug:product_slug>', product_detail,name='product_detail'),

#  path('product_detail/',product_detail,name='product_detail'),
]