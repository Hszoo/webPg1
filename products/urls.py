#urls.py

from django.contrib import admin
from django.urls import path, include
from products import views


urlpatterns = [
    path('', views.productHome, name="productHome"),
    path('', views.productSecond, name="productSecond")
 ]

# 127.0.0.1:8000/books/
# 127.0.0.1:8000/products/