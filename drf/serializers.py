from rest_framework import serializers
from .models import Products
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','product_name','description', 'price', 'image','stock']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password']