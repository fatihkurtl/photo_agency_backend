from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('content/', views.AboutUsContentViewSet.as_view({'get': 'list'}), name='about_us'),
    path('our_approach/', views.OurApproachViewSet.as_view({'get': 'list'}), name='our_approach'),
    path('business_card/', views.BusinessCardViewSet.as_view({'get': 'list'}), name='business_card'),
    path('skils_and_experience/', views.SkilsAndExperienceViewSet.as_view({'get': 'list'}), name='skils_and_experience'),
    path('achievements/', views.AchievementsViewSet.as_view({'get': 'list'}), name='achievements'),
]

urlpatterns = format_suffix_patterns(urlpatterns)