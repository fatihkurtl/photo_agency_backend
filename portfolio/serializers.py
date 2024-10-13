from rest_framework import serializers
from .models import Category, Work


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', 'created_at', 'updated_at')
        
    
class PortfolioSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Work
        exclude = ('id', 'created_at', 'updated_at')