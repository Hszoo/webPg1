#urls.py

from django.contrib import admin
from django.urls import path, include
from shops import views


urlpatterns = [
    path('', views.shopHome, name="shopHome"),
    path('', views.shopSecond, name="shopSecond")
 ]

# 127.0.0.1:8000/books/
# 127.0.0.1:8000/products/