# Generated by Django 5.1.1 on 2024-10-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herosection',
            name='title',
            field=models.CharField(help_text='Hero section başlığı', max_length=150, verbose_name='Hero Section Başlığı'),
        ),
    ]
