# Generated by Django 5.1.1 on 2024-10-13 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_package_features_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='features',
            field=models.ManyToManyField(help_text='Paket Özellikleri', related_name='packages_list', to='services.feature', verbose_name='Paket Özellikleri'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='package',
            field=models.ForeignKey(help_text='Paket', on_delete=django.db.models.deletion.CASCADE, related_name='features_list', to='services.package', verbose_name='Paket'),
        ),
    ]
