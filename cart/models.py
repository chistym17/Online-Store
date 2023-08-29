from django.db import models
from store.models import product

class Cart(models.Model):
    cart_id=models.CharField(max_length=10,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.cart_id
    
    
class CartItem(models.Model):
    product=models.OneToOneField(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_available=models.BooleanField(default=True)
    
    def count_total(self):
        return self.product.price* self.quantity
    
    def __str__(self) -> str:
        return str(self.product)

