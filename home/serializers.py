from rest_framework import serializers
from .models import HeroSection, CTASection



class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        exclude = ('id', 'created_at', 'updated_at')
        
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(obj.image.url)
                return url.replace('http://', 'https://')
            return obj.image.url.replace('http://', 'https://')
        return None


class CTASectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTASection
        exclude = ('id', 'created_at', 'updated_at')