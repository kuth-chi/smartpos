from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'  # For serving static files

class PublicMediaStorage(S3Boto3Storage):
    location = 'media/public'  # For serving public media files
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    location = 'media/private'  # For serving private media files
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
