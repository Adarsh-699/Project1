from django.urls import path
from . import views


urlpatterns = [
    path('cart_details/',views.show_cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item_from_cart,name='remove_item'),
    path('checkout_cart/',views.checkout_cart,name='checkout_cart'),
    path('orders/',views.show_orders,name='orders')
]
