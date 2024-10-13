from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('projects/', views.PortfolioViewSet.as_view({'get': 'list'}), name='portfolio'),
    path('projects/categories', views.CategoryViewSet.as_view({'get': 'list'}), name='category'),
]


urlpatterns = format_suffix_patterns(urlpatterns)