# Generated by Django 5.1.1 on 2024-10-13 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_package_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='features',
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('name', models.CharField(max_length=100, verbose_name='Özellik Adı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Özellik Açıklaması')),
                ('package', models.ForeignKey(help_text='Paket', on_delete=django.db.models.deletion.CASCADE, related_name='features', to='services.package', verbose_name='Paket')),
            ],
            options={
                'verbose_name': 'Paket Özelliği',
                'verbose_name_plural': 'Paket Özellikleri',
            },
        ),
    ]
