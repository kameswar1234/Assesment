from rest_framework import serializers
from .models import Items,Buy_Item

class Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class Buy_Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Buy_Item
        fields = '__all__'