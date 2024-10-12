from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import CustomerPortfolio, CustomerTestimonials, FeaturedProjects, SectoralRecognition


class CustomerPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPortfolio
        exclude = ('id', 'created_at', 'updated_at')
        
        
class CustomerTestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTestimonials
        exclude = ('id', 'created_at', 'updated_at')
        
        
class FeaturedProjectsSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = FeaturedProjects
        exclude = ('id', 'created_at', 'updated_at')
        

class SectoralRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectoralRecognition
        exclude = ('id', 'created_at', 'updated_at')