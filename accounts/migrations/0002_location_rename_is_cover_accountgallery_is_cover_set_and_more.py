# Generated by Django 4.2.5 on 2023-10-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("addressing", "0002_remove_country_leader_name_and_more"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("lat", models.FloatField(default=0.0, verbose_name="Latitude")),
                ("log", models.FloatField(default=0.0, verbose_name="Longitude")),
            ],
        ),
        migrations.RenameField(
            model_name="accountgallery",
            old_name="is_cover",
            new_name="is_cover_set",
        ),
        migrations.RemoveField(
            model_name="settinguser",
            name="is_dark",
        ),
        migrations.AddField(
            model_name="settinguser",
            name="date_format",
            field=models.CharField(
                blank=True,
                choices=[
                    ("%d-%m-%Y", "DD-MM-YYYY"),
                    ("%d-%m-%y", "DD-MM-YY"),
                    ("%a, %d %b %Y", "Mon, DD MMM YYYY"),
                    ("%A, %d %B %Y", "Mon, DD MMM YYYY"),
                    ("%B %d, %Y", "January DD, YYYY"),
                    ("%m-%d-%y", "MM-DD-YY"),
                    ("%m-%d-%Y", "MM-DD-YYYY"),
                    ("%y-%m-%d", "YY-MM-DD"),
                    ("%Y-%m-%d", "YYYY-MM-DD"),
                ],
                default="%d-%m-%Y",
                max_length=25,
                verbose_name="Date Format",
            ),
        ),
        migrations.AddField(
            model_name="settinguser",
            name="is_first_name",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="settinguser",
            name="theme",
            field=models.CharField(
                choices=[
                    ("dark", "Dark Mode"),
                    ("light", "Light Mode"),
                    ("auto", "System Mode"),
                ],
                default="auto",
                max_length=12,
                verbose_name="Theme Mode",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, upload_to="media/user/images/avatar/", verbose_name="Avatar"
            ),
        ),
        migrations.AlterField(
            model_name="accountgallery",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="media/user/images/account/", verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="settinguser",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("km", "Khmer")],
                default="en",
                max_length=25,
                verbose_name="Language",
            ),
        ),
        migrations.AlterField(
            model_name="settinguser",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accounts_UserSettings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("F", "Female"), ("M", "Male"), ("O", "Other")],
                default="O",
                max_length=10,
                verbose_name="Gender",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="user_set",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="primary_phone",
            field=models.CharField(
                blank=True, max_length=16, verbose_name="Primary phone"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                related_name="user_set_permissions",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="verificationaccount",
            name="dob",
            field=models.DateField(blank=True, verbose_name="date of birth"),
        ),
        migrations.CreateModel(
            name="UserAddress",
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
                        blank=True,
                        choices=[("home", "Home"), ("work", "Work")],
                        default=("home", "Home"),
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Address"
                    ),
                ),
                ("zip", models.PositiveBigIntegerField(blank=True, verbose_name="Zip")),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="address_city",
                        to="addressing.district",
                        verbose_name="City",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="address_country",
                        to="addressing.country",
                        verbose_name="Country",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="address_location",
                        to="accounts.location",
                        verbose_name="Location",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="address_province",
                        to="addressing.province",
                        verbose_name="State",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
    ]
