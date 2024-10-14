from django.db import models


class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        abstract = True


class General(CreatedUpdatedModel):
    company_name = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Firma Adı", help_text="Firma adı")
    logo = models.ImageField(upload_to="header", null=True, blank=True, verbose_name="Logo", help_text="Header logosu (firma logosu)")
    description = models.TextField(null=True, blank=True, verbose_name="Firma Açıklaması", help_text="Firma açıklaması, zorunlu değil footer için kullanılacak")
    
    class Meta:
        verbose_name = "Genel İçerik ( Header / Footer )"
        verbose_name_plural = "Genel İçerikler"
    
    def __str__(self):
        return self.company_name
    
    
class Offer(CreatedUpdatedModel):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Teklif Baslığı", help_text="Teklif baslığı")
    description = models.TextField(null=True, blank=True, verbose_name="Teklif Açıklaması", help_text="Teklif açıklaması")
    
    class Meta:
        verbose_name = "Teklif (Offer) İçeriği"
        verbose_name_plural = "Teklif (Offer) İçerikleri"
        
    def __str__(self):
        return self.title
    
    
class Seo(CreatedUpdatedModel):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Seo (Site) Başlığı", help_text="Seo (site) başlığı")
    description = models.TextField(null=False, blank=False, verbose_name="Seo (Site) Açıklaması", help_text="Seo (site) açıklaması")
    keywords = models.TextField(null=False, blank=False, verbose_name="Seo (Site) Anahtar Kelimeler", help_text="Seo (site) anahtar kelimeler, (a,b,c) şeklinde yazılmalıdır.")
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name="Seo (Site) Yazarı", help_text="Seo (site) yazarı")
    ogTitle = models.CharField(max_length=100, null=False, blank=False, verbose_name="Seo (Site) Og'nin Başlığı", help_text="Seo (site) Og'nin başlığı")
    ogDescription = models.TextField(null=False, blank=False, verbose_name="Seo (Site) Og'nin Açıklaması", help_text="Seo (site) Og'nin açıklaması")
    ogUrl = models.URLField(max_length=100, null=False, blank=False, verbose_name="Seo (Site) Og'nin Url", help_text="Seo (site) Og'nin url")
    ogImage = models.ImageField(upload_to="seo", null=False, blank=False, verbose_name="Seo (Site) Og'nin Resmi", help_text="Seo (site) Og'nin resmi")
    twitterTitle = models.CharField(max_length=100, null=False, blank=False, verbose_name="Seo (Site) Twitter Başlığı", help_text="Seo (site) Twitter başlığı")
    twitterDescription = models.TextField(null=False, blank=False, verbose_name="Seo (Site) Twitter Açıklaması", help_text="Seo (site) Twitter açıklaması")
    twitterImage = models.ImageField(upload_to="seo", null=False, blank=False, verbose_name="Seo (Site) Twitter Resmi", help_text="Seo (site) Twitter resmi")
    favicon = models.ImageField(upload_to="seo", null=False, blank=False, verbose_name="Seo (Site) Favicon", help_text="Seo (site) favicon resmi (.ico uzantılı dosyalar önerilir.)")
    
    class Meta:
        verbose_name = "Seo (Site) Ayarı"
        verbose_name_plural = "Seo (Site) Ayarları (Henüz kullanımda değil)"
        
    def __str__(self):
        return self.title