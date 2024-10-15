from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import HeroSection, CTASection
from .serializers import HeroSectionSerializer, CTASectionSerializer
import logging
logger = logging.getLogger(__name__)


class HeroSectionView(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        logger.debug(f"HeroSection data: {serializer.data}")
        return Response(serializer.data)


class CTASectionView(viewsets.ReadOnlyModelViewSet):
    queryset = CTASection.objects.all()
    serializer_class = CTASectionSerializer