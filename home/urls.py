from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('hero_section/', views.HeroSectionView.as_view({'get': 'list'}), name='hero_section'),
]


urlpatterns = format_suffix_patterns(urlpatterns)