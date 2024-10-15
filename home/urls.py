from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('hero_section/', views.HeroSectionView.as_view({'get': 'list'}), name='hero_section'),
    path('cta_section', views.CTASectionView.as_view({'get': 'list'}), name='cta_section'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)