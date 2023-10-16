# Generated by Django 4.2.5 on 2023-10-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="commune",
            name="is_public",
            field=models.BooleanField(blank=True, default=False, verbose_name="Public"),
        ),
        migrations.AddField(
            model_name="country",
            name="is_public",
            field=models.BooleanField(blank=True, default=False, verbose_name="Public"),
        ),
        migrations.AddField(
            model_name="district",
            name="is_public",
            field=models.BooleanField(blank=True, default=False, verbose_name="Public"),
        ),
        migrations.AddField(
            model_name="province",
            name="is_public",
            field=models.BooleanField(blank=True, default=False, verbose_name="Public"),
        ),
        migrations.AddField(
            model_name="village",
            name="is_public",
            field=models.BooleanField(blank=True, default=False, verbose_name="Public"),
        ),
    ]
