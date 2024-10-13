from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('content/', views.ServiceContentViewSet.as_view({'get': 'list'}), name='service_content'),
    path('packages/', views.ServiceViewSet.as_view({'get': 'list'}), name='services'),
    path('packages/categories/', views.CategoryViewSet.as_view({'get': 'list'}), name='categories'),
    path('why_choose_our_services/', views.WhyChooseOurServicesViewSet.as_view({'get': 'list'}), name='why_choose_our_services'),
]


urlpatterns = format_suffix_patterns(urlpatterns)