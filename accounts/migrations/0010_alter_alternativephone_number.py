# Generated by Django 4.2.5 on 2023-10-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_alter_alternativephone_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alternativephone",
            name="number",
            field=models.PositiveIntegerField(
                blank=True, unique=True, verbose_name="Number"
            ),
        ),
    ]