from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import HeroSection
from .serializers import HeroSectionSerializer


class HeroSectionView(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer


