from rest_framework import serializers
from .models import General, Offer, Seo


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        exclude = ('id', 'created_at', 'updated_at')
        

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        exclude = ('id', 'created_at', 'updated_at')
        
        
class SeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seo
        exclude = ('id', 'created_at', 'updated_at')