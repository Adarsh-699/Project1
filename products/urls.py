from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index_page'),  
    path('blank/',views.blank),
    path('products/',views.product_list,name='products'),
    path('product_details/<pk>',views.product_details,name='product_details'),
]
