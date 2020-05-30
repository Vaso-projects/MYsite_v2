from django.db import models
from time import strftime


class CreateHW(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100, unique=True, null=False)
    about = models.TextField(max_length=512, unique=True, null=False)
    image = models.FileField(null=False, upload_to='upload/img')
    file = models.FileField(null=False, upload_to='upload/HW')
    source = models.URLField(null=True)
