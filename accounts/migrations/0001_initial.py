# Generated by Django 4.2.5 on 2023-10-19 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("addressing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True, max_length=35, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=25, verbose_name="email"),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        upload_to="media/user/images/avatar/",
                        verbose_name="Avatar",
                    ),
                ),
                (
                    "primary_phone",
                    models.CharField(
                        blank=True, max_length=16, verbose_name="Primary phone"
                    ),
                ),
                (
                    "local_name",
                    models.CharField(
                        blank=True,
                        help_text="The name in your language",
                        max_length=50,
                        verbose_name="Local name",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="First name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Last name"
                    ),
                ),
                (
                    "dob",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of Birth"
                    ),
                ),
                (
                    "biography",
                    models.CharField(
                        blank=True,
                        help_text="Describe your self",
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "recovery_email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Recover Email",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("F", "Female"), ("M", "Male"), ("O", "Other")],
                        default="O",
                        max_length=10,
                        verbose_name="Gender",
                    ),
                ),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("joined_on", models.DateTimeField(auto_now_add=True)),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Public"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                ("is_staff", models.BooleanField(default=False, verbose_name="Staff")),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="Superuser"),
                ),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_set",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_set_permissions",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "unique_together": {("username", "email", "primary_phone")},
            },
        ),
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
                ("latitude", models.FloatField(default=0.0, verbose_name="Latitude")),
                ("longitude", models.FloatField(default=0.0, verbose_name="Longitude")),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialMedia",
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
                ("name", models.CharField(max_length=50)),
                ("url", models.URLField()),
                (
                    "custom_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/social_media_logos/"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerificationAccount",
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
                            ("passport", "Passport"),
                            ("id", "National Identity"),
                            ("other", "Other Identity"),
                        ],
                        default="passport",
                        max_length=150,
                        verbose_name="type",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="first_name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="last_name"),
                ),
                ("dob", models.DateField(blank=True, verbose_name="date of birth")),
                (
                    "social_reference",
                    models.TextField(
                        blank=True,
                        help_text="provide link of your profiles for more reference information",
                        max_length=500,
                        verbose_name="social_reference",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("reviewing", "Reviewing"),
                            ("rejected", "Rejected"),
                            ("verified", "Verified"),
                        ],
                        default="reviewing",
                        max_length=10,
                        verbose_name="status",
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserSocial",
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
                ("username", models.CharField(max_length=100)),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
                (
                    "social_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.socialmedia",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
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
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
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
                    "commune",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="address_commune",
                        to="addressing.commune",
                        verbose_name="Commune",
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
                (
                    "village",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="address_village",
                        to="addressing.village",
                        verbose_name="Village",
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.CreateModel(
            name="SettingUser",
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
                ("is_first_name", models.BooleanField(default=True)),
                (
                    "timezone",
                    models.CharField(
                        blank=True, max_length=25, verbose_name="Timezone"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("km", "Khmer")],
                        default="en",
                        max_length=25,
                        verbose_name="Language",
                    ),
                ),
                (
                    "date_format",
                    models.CharField(
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
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
                (
                    "theme",
                    models.CharField(
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
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts_UserSettings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AlternativePhone",
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
                        blank=True,
                        choices=[
                            ("mobile", "Mobile"),
                            ("home", "Home"),
                            ("work", "Work"),
                            ("other", "Other"),
                        ],
                        default="mobile",
                        max_length=20,
                        unique=True,
                        verbose_name="Type",
                    ),
                ),
                (
                    "number",
                    models.PositiveIntegerField(
                        blank=True, unique=True, verbose_name="Number"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alternative_phone",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ActiveDevice",
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
                        blank=True, max_length=100, verbose_name="Device's Name"
                    ),
                ),
                (
                    "os",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Device's OS"
                    ),
                ),
                (
                    "browser",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Browser"
                    ),
                ),
                (
                    "ip_address",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Device's IP Address"
                    ),
                ),
                (
                    "lat",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Latitude"
                    ),
                ),
                (
                    "log",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Longitude"
                    ),
                ),
                (
                    "last_login_time",
                    models.DateTimeField(auto_now=True, verbose_name="Last Login Time"),
                ),
                (
                    "login_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="Login Time"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "access_token",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Access Token"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="active_device",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AccountGallery",
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
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "is_avatar",
                    models.BooleanField(
                        default=False, unique=True, verbose_name="Is Avatar"
                    ),
                ),
                (
                    "is_cover_set",
                    models.BooleanField(default=False, verbose_name="Is cover"),
                ),
                (
                    "alt_image",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        verbose_name="alternative image image",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="media/user/images/account/",
                        verbose_name="image",
                    ),
                ),
                (
                    "uploaded_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Uploaded Date"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(auto_now=True, verbose_name="update at"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="submitted at"
                    ),
                ),
                (
                    "uploaded_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_gallery",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "AccountGallery",
                "verbose_name_plural": "AccountGalleries",
            },
        ),
    ]
