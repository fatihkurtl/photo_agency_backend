from django.db import models
from taggit.managers import TaggableManager


class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        abstract = True


class CustomerPortfolio(CreatedUpdatedModel):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Firma Adı", help_text="Firma adı")
    logo = models.ImageField(upload_to="references", null=True, blank=True, verbose_name="Firma Logosu", help_text="Firma logosu")
    
    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firma Portfolyosu"

    def __str__(self):
        return self.name
    

class CustomerTestimonials(CreatedUpdatedModel):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Müşteri Adı", help_text="Müşteri adı")
    company = models.CharField(max_length=100, null=False, blank=False, verbose_name="Firma Adı", help_text="Firma adı")
    image = models.ImageField(upload_to="references", null=True, blank=True, verbose_name="Müşteri Fotoğrafı", help_text="Müşteri fotoğrafı")
    quote = models.TextField(null=False, blank=False, verbose_name="Müşteri Görüşü", help_text="Müşteri görüşü")
    
    class Meta:
        verbose_name = "Müşteri Görüşü"
        verbose_name_plural = "Müşteri Görüşleri"

    def __str__(self):
        return self.name
    
    
class FeaturedProjects(CreatedUpdatedModel):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Proje Adı", help_text="Proje adı")
    description = models.TextField(null=False, blank=False, verbose_name="Açıklama", help_text="Açıklama")
    image = models.ImageField(upload_to="featured_projects", null=True, blank=True, verbose_name="Proje Fotoğrafı", help_text="Proje fotoğrafı")
    tags = TaggableManager(help_text="Virgülle ayrılmış etiketler(Tag1, Tag2, Tag3) gibi", verbose_name="Etiketler")
    
    class Meta:
        verbose_name = "Öne Çıkan Proje"
        verbose_name_plural = "Öne Çıkan Projeler"

    def __str__(self):
        return self.title
    
    
class SectoralRecognition(CreatedUpdatedModel):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Etkinlik", help_text="Etkinlik adı")
    description = models.CharField(max_length=500, null=False, blank=False, verbose_name="Açıklama", help_text="Etkinlik açıklaması")
    
    class Meta:
        verbose_name = "Etkinlik"
        verbose_name_plural = "Etkinlikler"
    
    def __str__(self):
        return self.title