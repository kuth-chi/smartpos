from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    A storage class for public media files.
    Inherits from S3Boto3Storage.
    """
    location = 'media'
    file_overwrite = False
    default_acl = 'public-read'
    
class PrivateMediaStorage(S3Boto3Storage):
    """
    A storage class for private media files.
    Inherits from S3Boto3Storage.
    """
    location = 'private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False