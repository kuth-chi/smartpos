# Generated by Django 4.2.5 on 2023-10-19 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Commune",
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
                    "type",
                    models.CharField(
                        choices=[("commune", "Commune"), ("sangkat", "Sangkat")],
                        default="commune",
                        max_length=10,
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=100, verbose_name="name"),
                ),
                (
                    "name_local",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local name"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True, max_length=3, verbose_name="Short name"
                    ),
                ),
                ("code", models.IntegerField(blank=True, verbose_name="Code")),
                (
                    "border_with",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Border with"
                    ),
                ),
                (
                    "border_length",
                    models.IntegerField(blank=True, verbose_name="Border length"),
                ),
                ("hotline", models.IntegerField(blank=True, verbose_name="Hotline")),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Public"
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                        blank=True, max_length=100, verbose_name="Country"
                    ),
                ),
                (
                    "name_local",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local name"
                    ),
                ),
                (
                    "flag",
                    models.ImageField(
                        blank=True,
                        upload_to="media/country/images/flag/",
                        verbose_name="Flag",
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True, max_length=3, verbose_name="Short name"
                    ),
                ),
                (
                    "code",
                    models.IntegerField(blank=True, default=0, verbose_name="Code"),
                ),
                (
                    "currency",
                    models.CharField(blank=True, max_length=3, verbose_name="Currency"),
                ),
                (
                    "primary_language",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Primary language"
                    ),
                ),
                (
                    "alt_languages",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Alternative languages"
                    ),
                ),
                (
                    "border_with",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=250,
                        verbose_name="Border with",
                    ),
                ),
                (
                    "border_length",
                    models.IntegerField(
                        blank=True, default=0, verbose_name="Border length"
                    ),
                ),
                (
                    "landmark",
                    models.IntegerField(blank=True, default=0, verbose_name="Landmark"),
                ),
                ("is_before_chris", models.BooleanField(blank=True, default=False)),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Public"
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="Village",
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
                    models.CharField(blank=True, max_length=100, verbose_name="name"),
                ),
                (
                    "name_local",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local name"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True, max_length=3, verbose_name="Short name"
                    ),
                ),
                ("code", models.IntegerField(blank=True, verbose_name="Code")),
                (
                    "border_with",
                    models.CharField(
                        blank=True,
                        default=False,
                        max_length=250,
                        verbose_name="Border with",
                    ),
                ),
                (
                    "border_length",
                    models.IntegerField(blank=True, verbose_name="Border length"),
                ),
                ("hotline", models.IntegerField(blank=True, verbose_name="Hotline")),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Public"
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="Timestamp"),
                ),
                (
                    "commune_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="addressing.commune",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Province",
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
                    "type",
                    models.CharField(
                        choices=[("province", "Province"), ("capital", "Capital")],
                        default="province",
                        max_length=10,
                        verbose_name="Type",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=100, verbose_name="name"),
                ),
                (
                    "name_local",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local name"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True, max_length=3, verbose_name="Short name"
                    ),
                ),
                ("code", models.IntegerField(blank=True, verbose_name="Code")),
                (
                    "border_with",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Border with"
                    ),
                ),
                (
                    "border_length",
                    models.IntegerField(blank=True, verbose_name="Border length"),
                ),
                (
                    "leader",
                    models.CharField(blank=True, max_length=25, verbose_name="Leader"),
                ),
                ("hotline", models.IntegerField(verbose_name="Hotline")),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Public"
                    ),
                ),
                ("latitude", models.FloatField(blank=True, verbose_name="Latitude")),
                ("longitude", models.FloatField(blank=True, verbose_name="Longitude")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "country_id",
                    models.ForeignKey(
                        blank=True,
                        default=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="province",
                        to="addressing.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="District",
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
                    "type",
                    models.CharField(
                        choices=[
                            ("district", "District"),
                            ("khan", "Khan"),
                            ("city", "City"),
                        ],
                        default="district",
                        max_length=10,
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=100, verbose_name="name"),
                ),
                (
                    "name_local",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local name"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True, max_length=3, verbose_name="Short name"
                    ),
                ),
                ("code", models.IntegerField(blank=True, verbose_name="Code")),
                (
                    "border_with",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Border with"
                    ),
                ),
                (
                    "border_length",
                    models.IntegerField(blank=True, verbose_name="Border length"),
                ),
                ("hotline", models.IntegerField(blank=True, verbose_name="Hotline")),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Public"
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="timestamp"),
                ),
                (
                    "province_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="district",
                        to="addressing.province",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CountryLeader",
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
                    "first_name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Fist name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Last name"
                    ),
                ),
                (
                    "local_name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local name"
                    ),
                ),
                (
                    "gender",
                    models.CharField(blank=True, max_length=100, verbose_name="Gender"),
                ),
                ("born", models.DateField(blank=True, verbose_name="Born")),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("prime_minister", "Prime Minister"),
                            ("president", "President"),
                        ],
                        default="prime_minister",
                        max_length=100,
                        verbose_name="Position",
                    ),
                ),
                ("start_on", models.DateField(blank=True, verbose_name="Start on")),
                ("exit_on", models.DateField(blank=True, verbose_name="Exit on")),
                (
                    "contributor",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Contributor"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "country_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="country_leader",
                        to="addressing.country",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="commune",
            name="district_id",
            field=models.ForeignKey(
                blank=True,
                default=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="commune",
                to="addressing.district",
            ),
        ),
    ]
