from django.db import models


class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        abstract = True
        

class ContactForm(CreatedUpdatedModel):
    firstname = models.CharField(max_length=60, null=False, blank=False, verbose_name="Adı", help_text="Adı")
    lastname = models.CharField(max_length=60, null=False, blank=False, verbose_name="Soyadı", help_text="Soyadı")   
    email = models.EmailField(null=False, blank=False, verbose_name="E-posta", help_text="E-posta adresi")
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name="Telefon numarası", help_text="Telefon numarası")
    service = models.CharField(max_length=60, null=False, blank=False, verbose_name="Hizmet", help_text="Hizmet")
    date = models.CharField(max_length=50, null=False, blank=False, verbose_name="Tarih", help_text="Tarih")
    time = models.CharField(max_length=50, null=False, blank=False, verbose_name="Saat", help_text="Saat")
    content = models.TextField(null=False, blank=False, verbose_name="Mesaj", help_text="Mesaj içeriği")
    
    class Meta:
        verbose_name = "İletişim Formu"
        verbose_name_plural = "İletişim Formları"
        
    
    def __str__(self):
        return f"iletişim formu ({self.email})"

class ContactInformation(CreatedUpdatedModel):
    address = models.TextField(null=True, blank=True, verbose_name="Adres", help_text="Adres bilgisi")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefon numarası", help_text="Telefon bilgisi")
    email = models.EmailField(null=True, blank=True, verbose_name="E-posta", help_text="E-posta bilgisi")
    work_hours = models.TextField(null=True, blank=True, verbose_name="Çalışma saatleri", help_text="Çalışma günleri ve saatleri / (Pazartesi - Cuma: 09.00 - Akşam : 18.00)")

    class Meta:
        verbose_name = "İletişim Bilgisi"
        verbose_name_plural = "İletişim Bilgileri"

    def __str__(self):
        return f"İletişim bilgileri ({self.email})"


class SocialMedia(CreatedUpdatedModel):
    name = models.CharField(max_length=50, verbose_name="Adı", help_text="Sosyal medya adı")
    url = models.URLField(verbose_name="URL", help_text="Sosyal medya adresi")

    class Meta:
        verbose_name = "Sosyal Medya"
        verbose_name_plural = "Sosyal Medya"

    def __str__(self):
        return self.name


class WhyChooseUs(CreatedUpdatedModel):
    title = models.CharField(max_length=50, verbose_name="Başlık", help_text="Hakkımızda başlığı")
    description = models.TextField(verbose_name="Açıklama", help_text="Hakkımızda açıklaması")

    class Meta:
        verbose_name = "Neden Biz"
        verbose_name_plural = "Neden Biz"

    def __str__(self):
        return self.title


class FrequentlyAskedQuestions(CreatedUpdatedModel):
    question = models.CharField(max_length=250, verbose_name="Soru", help_text="Soru")
    answer = models.TextField(verbose_name="Cevap", help_text="Cevap")

    class Meta:
        verbose_name = "Sıkça Sorulan Soru"
        verbose_name_plural = "Sıkça Sorulan Sorular"

    def __str__(self):
        return self.question
