from django.db import models


class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        abstract = True
        

class Category(CreatedUpdatedModel):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Kategori Adı", help_text="Kategori Adı")
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Kategori Slug", help_text="Kategori filtreleme kısmı (Kategori adı ile aynı ama küçük harflerle olmalıdır)")
    
    class Meta:
        verbose_name = "Hizmet Kategorisi"
        verbose_name_plural = "Hizmet Kategorileri"

    def __str__(self):
        return f"{self.name} - {self.slug}"
    

class Service(CreatedUpdatedModel):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Hizmet Adı", help_text="Hizmet Adı")
    description = models.TextField(null=False, blank=False, verbose_name="Hizmet Açıklaması", help_text="Hizmet Açıklaması")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services", verbose_name="Hizmet Kategorisi", help_text="Hizmet kategorisi")
    
    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"

    def __str__(self):
        return self.title
    

class Package(CreatedUpdatedModel):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Paket Adı", help_text="Paket Adı")
    price = models.CharField(max_length=20, null=True, blank=True, verbose_name="Paket Fiyatı", help_text="Paket Fiyatı")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True, related_name="packages", verbose_name="Hizmet", help_text="Paket eklemek istediğiniz hizmeti seçin.")
    
    class Meta:
        verbose_name = "Hizmet Paketi"
        verbose_name_plural = "Hizmet Paketleri"

    def __str__(self):
        return f"{self.service.title or ''} - {self.name}"
    

class Feature(CreatedUpdatedModel):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="features", verbose_name="Paket", help_text="Özellik eklemek istediğiniz paketi seçin.")
    description = models.CharField(max_length=255, verbose_name="Özellik Açıklaması", help_text="Özellik açıklaması, madde madde ekleneceği için tek satırlık eklemeler önerilir.")

    class Meta:
        verbose_name = "Paket Özelliği"
        verbose_name_plural = "Paket Özellikleri"

    def __str__(self):
        return f"{self.package.name} - {self.description}"