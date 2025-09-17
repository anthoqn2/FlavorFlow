from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import IngredientSerializer
from .models import Ingredient

# Create your views here.
def home(request):
    return render(request, 'main.html')

@api_view(['GET'])
def get_data(request):
    data = {
        'flavor': 'Vanilla'
    }
    print("get request")
    return Response(data)

@api_view(['POST'])
def add_ingredient(request):
    print(f"adding ingredient {request.data}")
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # saves directly to Django DB
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_data(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)
