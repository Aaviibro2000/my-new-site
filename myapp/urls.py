from django.urls import include, path

from .views import add_product, index, products, products_details

urlpatterns = [
    path('',index),
    path('products',products),
    path('products/<int:id>',products_details),
    path('add_product/',add_product)
    
]