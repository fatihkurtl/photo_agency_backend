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
        verbose_name = "Portfolyo Kategorisi"
        verbose_name_plural = "Portfolyo Kategorileri"

    def __str__(self):
        return self.name
    

class Work(CreatedUpdatedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori", help_text="Portfolyo kategorisi")
    image = models.ImageField(upload_to="portfolio", null=True, blank=True, verbose_name="Fotoğraf", help_text="Fotoğraf")
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Fotoğraf Adı", help_text="Fotoğraf Adı / Proje Adı")
    
    class Meta:
        verbose_name = "Portfolyo Fotoğrafı"
        verbose_name_plural = "Portfolyo Fotoğrafları"

    def __str__(self):
        return self.name
    