# Generated by Django 4.2.5 on 2023-10-08 03:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_remove_location_log_location_lon"),
    ]

    operations = [
        migrations.RenameField(
            model_name="location",
            old_name="lat",
            new_name="latitude",
        ),
        migrations.RenameField(
            model_name="location",
            old_name="lon",
            new_name="longitude",
        ),
    ]