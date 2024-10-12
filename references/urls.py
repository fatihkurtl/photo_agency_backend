from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('customer_portfolio/', views.CustomerPortfolioViewSet.as_view({'get': 'list'}), name='customer_portfolio'),
    path('customer_testimonials/', views.CustomerTestimonialsViewSet.as_view({'get': 'list'}), name='customer_testimonials'),
    path('featured_projects/', views.FeaturedProjectsViewSet.as_view({'get': 'list'}), name='featured_projects'),
    path('sectoral_recognition/', views.SectoralRecognitionViewSet.as_view({'get': 'list'}), name='sectoral_recognition'),
]


urlpatterns = format_suffix_patterns(urlpatterns)