'''Takes the model and converts it to a JSON object and validates the data
Fetch: MongoDB -> Django -> Serializer -> JSON -> React 
Create: Serializer -> Django -> MongoDB
Update: Serializer -> Django -> MongoDB
Delete: Django -> MongoDB
'''

from rest_framework import serializers
from .models import Ingredient, Amount


class AmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount
        fields = ['id','value','measurement_type']

class IngredientSerializer(serializers.ModelSerializer):
    amount = AmountSerializer()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Ingredient 
        fields = ['id','name','amount','category','category_display']
