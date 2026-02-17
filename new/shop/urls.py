from django.urls import path
from . import views

urlpatterns = [
    path('shoplist/', views.shopList, name="shopList"),
    path('shopdetail/', views.shopDetail, name = "shopDetail"),
]