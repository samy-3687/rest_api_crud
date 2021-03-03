from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Products
from testapp.serializers import ProductSerializer

# Create your views here.
class ProductCRUDCBV(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class = ProductSerializer