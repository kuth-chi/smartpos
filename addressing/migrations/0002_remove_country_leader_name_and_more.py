# Generated by Django 4.2.5 on 2023-10-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressing", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="country",
            name="leader_name",
        ),
        migrations.AlterField(
            model_name="country",
            name="border_length",
            field=models.IntegerField(
                blank=True, default=0, verbose_name="Border length"
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="border_with",
            field=models.CharField(
                blank=True, default="", max_length=250, verbose_name="Border with"
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="code",
            field=models.IntegerField(blank=True, default=0, verbose_name="Code"),
        ),
        migrations.AlterField(
            model_name="country",
            name="landmark",
            field=models.IntegerField(blank=True, default=0, verbose_name="Landmark"),
        ),
    ]
