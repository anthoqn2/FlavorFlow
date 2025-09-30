from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Ingredient

# Create your views here.
def home(request):
    return render(request, 'main.html')


#Adding ingredient to user's pantry
'''
Receives json like "{'name': 'water', 'category': 'vegetable', 'value': '1', 'unit': 'grams'}"
'''
@api_view(['POST'])
def add_ingredient(request):
    print(f"adding ingredient {request.data}")
    ingred = Ingredient(name = request.data.get('name'), category = request.data.get('category'), value = request.data.get('value'), unit = request.data.get('unit'))
    ingred.save()
    return Response({"message": "Ingredient added!"}, status=status.HTTP_201_CREATED)
    

#Getting all pantry items from user 
@api_view(['GET'])
def get_data(request):
    print("Getting all ingredients")

    ingredients = Ingredient.objects.all()
    data = []
    for ing in ingredients:
        data.append({
            "name": ing.name,
            "category": ing.category,
            "value": ing.value,
            "unit": ing.unit
        })

    return Response(data = data, status=status.HTTP_200_OK)
