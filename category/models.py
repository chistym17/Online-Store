from django.db import models

class category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.CharField(max_length=220,blank=True)
    category_image=models.ImageField(upload_to='photos/categories',blank=True)
    
    def __str__(self) -> str:
        return self.category_name