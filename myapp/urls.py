from django.urls import include, path

from .views import index, products

urlpatterns = [
    path('',index),
    path('products',products),
]
