# Generated by Django 5.1.1 on 2024-10-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_package_name_package_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(blank=True, help_text='Paket Adı', max_length=100, null=True, verbose_name='Paket Adı'),
        ),
    ]
