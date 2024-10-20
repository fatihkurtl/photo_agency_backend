# Generated by Django 5.1.1 on 2024-10-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, help_text='Adres bilgisi', null=True, verbose_name='Adres')),
                ('phone', models.CharField(blank=True, help_text='Telefon bilgisi', max_length=20, null=True, verbose_name='Telefon numarası')),
                ('email', models.EmailField(blank=True, help_text='E-posta bilgisi', max_length=254, null=True, verbose_name='E-posta')),
                ('work_hours', models.TextField(blank=True, help_text='Çalışma günleri ve saatleri / (Pazartesi - Cuma: 09.00 - Akşam : 18.00)', null=True, verbose_name='Çalışma saatleri')),
            ],
            options={
                'verbose_name': 'İletişim bilgisi',
                'verbose_name_plural': 'İletişim bilgileri',
            },
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Soru', max_length=250, verbose_name='Soru')),
                ('answer', models.TextField(help_text='Cevap', verbose_name='Cevap')),
            ],
            options={
                'verbose_name': 'Sıkça sorulan soru',
                'verbose_name_plural': 'Sıkça sorulan sorular',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sosyal medya adı', max_length=50, verbose_name='Adı')),
                ('url', models.URLField(help_text='Sosyal medya adresi', verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Sosyal medya',
                'verbose_name_plural': 'Sosyal medya',
            },
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Hakkımızda başlığı', max_length=50, verbose_name='Başlık')),
                ('description', models.TextField(help_text='Hakkımızda açıklaması', verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Neden Biz',
                'verbose_name_plural': 'Neden Biz',
            },
        ),
    ]
