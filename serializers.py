from .models import GroceryList
from rest_framework import serializers

class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = groceryapi
        fields = ('name')