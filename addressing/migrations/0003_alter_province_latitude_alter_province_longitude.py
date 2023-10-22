# Generated by Django 4.2.5 on 2023-10-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressing", "0002_alter_province_latitude_alter_province_longitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="province",
            name="latitude",
            field=models.FloatField(blank=True, default=0.0, verbose_name="Latitude"),
        ),
        migrations.AlterField(
            model_name="province",
            name="longitude",
            field=models.FloatField(blank=True, default=0.0, verbose_name="Longitude"),
        ),
    ]
