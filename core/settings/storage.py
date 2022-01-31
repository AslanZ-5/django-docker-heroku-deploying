import os

from pathlib import Path

from core.settings.settings import BASE_DIR 
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Boto3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'AKIARTHVHMINHL3C6TFQ'
AWS_SECRET_ACCESS_KEY ='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'
AWS_STORAGE_BUCKET_NAME ='djanog'
AWS_DEFAULT_ACL = None
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.us-east-1.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

# A path prefix that will be prepended to all uploads
AWS_LOCATION = 'static'
STATIC_URL = f'https://{S3_URL}/{AWS_LOCATION}/'




# Django Static Files Directory
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)




