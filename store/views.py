from django.shortcuts import render,get_object_or_404
from .models import product
from category.models import category
from django.core.paginator import Paginator
def store(request,category_slug=None):
    products=None
    Category=None
    if category_slug:
            Category=get_object_or_404(category,slug=category_slug)

            products=product.objects.filter(is_available=True,category=Category)
            paginator=Paginator(products,1)
            page = request.GET.get('page')

            paged_product=paginator.get_page(page)


    else:
        products=product.objects.filter(is_available=True)
        paginator=Paginator(products,1)
        page = request.GET.get('page')

        paged_product=paginator.get_page(page)



    categories=category.objects.all()
    context={
    'products':products,
    'categories':categories
        
    }
    return render(request,'store/store.html',context)

def product_detail(request,category_slug,product_slug):
    clicked_product = product.objects.get(slug=product_slug, category__slug=category_slug)

    return render(request,'store/product_detail.html',{'product':clicked_product})