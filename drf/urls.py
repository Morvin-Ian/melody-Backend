from django.urls import path
from . import views

from .views import ProductList, ProductDetail, UserList, UserDetail


urlpatterns = [

    # Products
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),

     # Users
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]

