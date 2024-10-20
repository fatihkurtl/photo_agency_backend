# Generated by Django 5.1.1 on 2024-10-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_general_delete_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('description', models.TextField(blank=True, help_text='Footer açıklaması, zorunlu değil.', null=True, verbose_name='Footer Açıklama')),
            ],
            options={
                'verbose_name': 'Footer İçeriği',
                'verbose_name_plural': 'Footer İçerikleri',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('company_name', models.CharField(help_text='Firma adı', max_length=100, unique=True, verbose_name='Firma Adı')),
                ('logo', models.ImageField(blank=True, help_text='Header logosu (şirket logosu)', null=True, upload_to='header', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Header İçeriği',
                'verbose_name_plural': 'Header İçerikleri',
            },
        ),
        migrations.DeleteModel(
            name='General',
        ),
    ]
