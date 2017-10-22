from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class GroceryListGets(APIView):
    def get(request, format=None):
        groceryItems = GroceryList.objects.all()
        groceryItems_serializer = CountrySerializer(groceryItems, many=True)
        return Response(groceryItems_serializer.data)