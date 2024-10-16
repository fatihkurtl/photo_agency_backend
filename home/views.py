from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import HeroSection, CTASection
from .serializers import HeroSectionSerializer, CTASectionSerializer


class HeroSectionView(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CTASectionView(viewsets.ReadOnlyModelViewSet):
    queryset = CTASection.objects.all()
    serializer_class = CTASectionSerializer