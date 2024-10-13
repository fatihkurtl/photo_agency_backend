from django.db import models

class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        abstract = True
        

class AboutUsContent(CreatedUpdatedModel):
    title = models.CharField(max_length=50, verbose_name="Hakkımızda Başlık", help_text="Hakkımızda başlığı giriniz.")
    content = models.TextField(verbose_name="Hakkımızda İçerik", help_text="Hakkımızda içeriği giriniz.")
    
    class Meta:
        verbose_name = "Hakkımızda İçeriği"
        verbose_name_plural = "Hakkımızda İçerikleri"
        
    def __str__(self):
        return self.title


class OurApproach(CreatedUpdatedModel):
    title = models.CharField(max_length=50, verbose_name="Yaklaşımımız Başlık", help_text="Yaklaşımımız başlığı giriniz.")
    content = models.TextField(verbose_name="Yaklaşımımız İçerik", help_text="Yaklaşımımız içeriği giriniz.")
    
    class Meta:
        verbose_name = "Yaklaşımımız İçeriği"
        verbose_name_plural = "Yaklaşımımız İçerikleri"
        
    def __str__(self):
        return self.title
    

class BusinessCard(CreatedUpdatedModel):
    logo = models.ImageField(upload_to="about", null=True, blank=True, verbose_name="Logo", help_text="Logo")
    title = models.CharField(max_length=50, verbose_name="Başlık", help_text="Kartvizit başlığı")
    subtitle = models.CharField(max_length=50, verbose_name="Alt Başlık", help_text="Kartvizit alt başlığı")
    
    class Meta:
        verbose_name = "Kartvizit İçeriği"
        verbose_name_plural = "Kartvizit İçerikleri"
        
    def __str__(self):
        return self.title
    

class SkilsAndExperience(CreatedUpdatedModel):
    content = models.CharField(max_length=100, verbose_name="İçerik", help_text="İçerik")
    
    class Meta:
        verbose_name = "Beceriler ve Uzmanlık"
        verbose_name_plural = "Beceriler ve Uzmanlıklar"
        
    def __str__(self):
        return self.content
    

class Achievements(CreatedUpdatedModel):
    year = models.CharField(max_length=4, verbose_name="Yıl", help_text="Yıl")
    content = models.CharField(max_length=2000, verbose_name="İçerik", help_text="İçerik")
    
    class Meta:
        verbose_name = "Başarılarımız"
        verbose_name_plural = "Başarılarımız"
        
    def __str__(self):
        return self.content
