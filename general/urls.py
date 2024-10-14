from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.GeneralViewSet.as_view({'get': 'list'}), name='general'),
    path('offer/', views.OfferViewSet.as_view({'get': 'list'}), name='offer'),
    path('seo/', views.SeoViewSet.as_view({'get': 'list'}), name='seo'),
]


urlpatterns = format_suffix_patterns(urlpatterns)