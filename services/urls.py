from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('packages/', views.ServiceViewSet.as_view({'get': 'list'}), name='services'),
    path('packages/categories/', views.CategoryViewSet.as_view({'get': 'list'}), name='categories'),
]


urlpatterns = format_suffix_patterns(urlpatterns)