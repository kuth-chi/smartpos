# Generated by Django 4.2.5 on 2023-09-30 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("uuid", models.UUIDField(unique=True)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, upload_to="org/logo")),
                ("header_cover", models.ImageField(blank=True, upload_to="org/cover")),
                ("description", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="SocialProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("website", "Website"),
                            ("facebook", "Facebook"),
                            ("youtube", "YouTube"),
                            ("instragram", "Instagram"),
                            ("x", "X"),
                            ("linkedin", "LinkedIn"),
                            ("tiktok", "Tiktok"),
                            ("discord", "Discord"),
                            ("snapchat", "Snapchat"),
                            ("whatsapp", "WhatsApp"),
                            ("telegram", "Telegram"),
                        ],
                        max_length=100,
                        verbose_name="Social Profile",
                    ),
                ),
                ("link", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.organization",
                    ),
                ),
            ],
        ),
    ]
