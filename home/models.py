from django.db import models


class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        abstract = True
        

class HeroSection(CreatedUpdatedModel):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Hero Section Başlığı", help_text="Hero section başlığı")
    description = models.TextField(verbose_name="Hero Section Açıklama", help_text="Her section açıklaması")
    image = models.ImageField(upload_to="home", verbose_name="Hero Section Fotoğrafı", help_text="Hero section fotoğrafı")

    class Meta:
        verbose_name = "Home Hero Section"
        verbose_name_plural = "Hero Sections"
        
    def __str__(self):
        return self.title
