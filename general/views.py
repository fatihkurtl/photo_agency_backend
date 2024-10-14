from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import General, Offer, Seo
from .serializers import GeneralSerializer, OfferSerializer, SeoSerializer


class GeneralViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer


class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    
    
class SeoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Seo.objects.all()
    serializer_class = SeoSerializer