from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:8]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

def blank(request):
    return render(request,'blank_layout.html')



def product_details(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_details.html',context)

def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page')
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,3)
    product_list=product_paginator.get_page(page)
    context ={'products':product_list}
    return render(request,'products.html',context)