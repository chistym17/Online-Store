from django.contrib import admin
from .models import category
# Register your models here.

class category_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','slug')
    
    
admin.site.register(category,category_admin)
