from rest_framework import serializers
from .models import HeroSection, CTASection



class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        exclude = ('id', 'created_at', 'updated_at')


class CTASectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTASection
        exclude = ('id', 'created_at', 'updated_at')