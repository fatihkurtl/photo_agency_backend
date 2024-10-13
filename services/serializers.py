from rest_framework import serializers
from .models import Category, Package, Service, Feature

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        exclude = ('id', 'created_at', 'updated_at')
        

class PackageSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Package
        exclude = ('id', 'created_at', 'updated_at')

    def get_features(self, obj):
        return [feature.description for feature in obj.features.all()]
    

class ServiceSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        exclude = ('id', 'created_at', 'updated_at')
        

class CategorySerializer(serializers.ModelSerializer):
    # services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ('id', 'created_at', 'updated_at')
        

class ServiceListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    packages = PackageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        exclude = ('id', 'created_at', 'updated_at')