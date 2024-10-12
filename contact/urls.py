from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('us/', views.ContactSaveView.as_view(), name='contact_save'),
    path('information/', views.ContactInformationViewSet.as_view({'get': 'list'}), name='contact'),
    path('social_media_accounts/', views.SocialMediaViewSet.as_view({'get': 'list'}), name='social'),
    path('why_choose_us/', views.WhyChooseUsViewSet.as_view({'get': 'list'}), name='choose_us'),
    path('faq/', views.FrequentlyAskedQuestionsViewSet.as_view({'get': 'list'}), name='faq'),
]

urlpatterns = format_suffix_patterns(urlpatterns)