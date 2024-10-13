from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import ServiceContent, Category, Service, WhyChooseOurServices
from .serializers import ServiceContentSerializer, CategorySerializer, ServiceListSerializer, WhyChooseOurServicesSerializer



class ServiceContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceContent.objects.all()
    serializer_class = ServiceContentSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceListSerializer
    
    
class WhyChooseOurServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WhyChooseOurServices.objects.all()
    serializer_class = WhyChooseOurServicesSerializer