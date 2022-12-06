from django.urls import include, path

from .views import add_product, index, products, products_details,update_product

urlpatterns = [
    path('',index),
    path('products',products,name='products'),
    path('products/<int:id>',products_details,name='products_details'),
    path('products/add',add_product,name='add_product'),
    path('products/update/<int:id>',update_product,name='update_product'),
    
]