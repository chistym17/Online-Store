from django.contrib import admin
from .models import product
# Register your models here.

class product_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name','price','is_available','stock','created_date','modified_date')
    
    
admin.site.register(product,product_admin)
