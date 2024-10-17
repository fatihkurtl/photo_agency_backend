"""
URL configuration for photo_agency_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = "FA Medya Admin Paneli"
admin.site.site_title = "FA Medya Admin Paneli"
admin.site.index_title = "FA Medya Admin Paneline Hoş geldiniz"

urlpatterns = [
    path('fa_medya_yönetim/', admin.site.urls),
    path("admin/",include("admin_honeypot.urls")),
    path('api/', include([
        path('contact/', include('contact.urls')),
        path('about/', include('about.urls')),
        path('references/', include('references.urls')),
        path('portfolio/', include('portfolio.urls')),
        path('services/', include('services.urls')),
        path('home/', include('home.urls')),
        path('general/', include('general.urls')),
    ])),
    path("api-auth/", include("rest_framework.urls"), name="rest_framework"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)