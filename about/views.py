from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import AboutUsContent, OurApproach, BusinessCard, SkilsAndExperience, Achievements
from .serializers import AboutUsContentSerializer, OurApproachSerializer, BusinessCardSerializer, SkilsAndExperienceSerializer, AchievementsSerializer


class AboutUsContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUsContent.objects.all()
    serializer_class = AboutUsContentSerializer
    

class OurApproachViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OurApproach.objects.all()
    serializer_class = OurApproachSerializer
    

class BusinessCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusinessCard.objects.all()
    serializer_class = BusinessCardSerializer
    

class SkilsAndExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SkilsAndExperience.objects.all()
    serializer_class = SkilsAndExperienceSerializer
    

class AchievementsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer