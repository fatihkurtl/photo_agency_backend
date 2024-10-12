from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import CustomerPortfolio, CustomerTestimonials, FeaturedProjects, SectoralRecognition
from .serializers import CustomerPortfolioSerializer, CustomerTestimonialsSerializer, FeaturedProjectsSerializer, SectoralRecognitionSerializer


class CustomerPortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerPortfolio.objects.all()
    serializer_class = CustomerPortfolioSerializer


class CustomerTestimonialsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerTestimonials.objects.all()
    serializer_class = CustomerTestimonialsSerializer
    

class FeaturedProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeaturedProjects.objects.all()
    serializer_class = FeaturedProjectsSerializer
    

class SectoralRecognitionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SectoralRecognition.objects.all()
    serializer_class = SectoralRecognitionSerializer