from rest_framework import serializers
from .models import HeroSection



class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        exclude = ('id', 'created_at', 'updated_at')


