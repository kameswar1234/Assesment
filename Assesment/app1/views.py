from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView
from .serializer import Item_Serializer,Buy_Item_Serializer
from .models import Items,Buy_Item
# Create your views here.

class GetItems(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = Item_Serializer


class Buy_Items(CreateAPIView):
    queryset = Buy_Item.objects.all()
    serializer_class = Buy_Item_Serializer

class Update_Items(UpdateAPIView):
    queryset = Buy_Item.objects.all()
    serializer_class = Buy_Item_Serializer