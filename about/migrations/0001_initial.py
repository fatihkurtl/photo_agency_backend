# Generated by Django 5.1.1 on 2024-10-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('title', models.CharField(help_text='Hakkımızda başlığı giriniz.', max_length=50, verbose_name='Hakkımızda Başlık')),
                ('content', models.TextField(help_text='Hakkımızda içeriği giriniz.', verbose_name='Hakkımızda İçerik')),
            ],
            options={
                'verbose_name': 'Hakkımızda İçeriği',
                'verbose_name_plural': 'Hakkımızda İçerikleri',
            },
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('year', models.CharField(help_text='Yıl', max_length=4, verbose_name='Yıl')),
                ('content', models.CharField(help_text='İçerik', max_length=2000, verbose_name='İçerik')),
            ],
            options={
                'verbose_name': 'Başarılarımız',
                'verbose_name_plural': 'Başarılarımız',
            },
        ),
        migrations.CreateModel(
            name='BusinessCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('logo', models.ImageField(blank=True, help_text='Logo', null=True, upload_to='about', verbose_name='Logo')),
                ('title', models.CharField(help_text='Business Card başlığı', max_length=50, verbose_name='Başlık')),
                ('subtitle', models.CharField(help_text='Business Card alt başlığı', max_length=50, verbose_name='Alt Başlık')),
            ],
            options={
                'verbose_name': 'Business Card İçeriği',
                'verbose_name_plural': 'Business Cards İcerikleri',
            },
        ),
        migrations.CreateModel(
            name='OurApproach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('title', models.CharField(help_text='Yaklaşımımız başlığı giriniz.', max_length=50, verbose_name='Yaklaşımımız Başlık')),
                ('content', models.TextField(help_text='Yaklaşımımız içeriği giriniz.', verbose_name='Yaklaşımımız İçerik')),
            ],
            options={
                'verbose_name': 'Yaklaşımımız İçeriği',
                'verbose_name_plural': 'Yaklaşımımız İcerikleri',
            },
        ),
        migrations.CreateModel(
            name='SkilsAndExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('content', models.CharField(help_text='İçerik', max_length=100, verbose_name='İçerik')),
            ],
            options={
                'verbose_name': 'Beceriler ve Uzmanlık',
                'verbose_name_plural': 'Beceriler ve Uzmanlıklar',
            },
        ),
    ]
