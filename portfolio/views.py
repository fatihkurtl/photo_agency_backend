from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Category, Work
from .serializers import CategorySerializer, PortfolioSerializer 


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all().order_by('-created_at')
    serializer_class = PortfolioSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer