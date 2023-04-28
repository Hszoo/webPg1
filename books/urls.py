#urls.py

from django.contrib import admin
from django.urls import path, include
from books import views


urlpatterns = [
    path('', views.bookHome, name="bookHome"),
    path('', views.bookSecond, name="bookSecond")
 ]

# 127.0.0.1:8000/books/
# 127.0.0.1:8000/products/