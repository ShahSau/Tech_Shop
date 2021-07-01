from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from.models import Product

from .product import products
from .serializers import ProductSerializer, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        # data['username'] = self.user.username
        # data['email'] = self.user.email

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/products/', 
        '/api/products/create/',

        '/api/products/upload',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>',   

        '/api/products/delete/<id>/', 
        '/api/products/<update>/<id>/',   

    ]
    return Response(routes)

@api_view(['GET'])
def getUserProfile(request):
    user =request.user
    
    serializers = UserSerializer(user, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getProducts(request):
    serializers = ProductSerializer(products, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializers = ProductSerializer(product, many=False)
    return Response(serializers.data)