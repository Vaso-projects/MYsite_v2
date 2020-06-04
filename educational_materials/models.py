from django.db import models
from time import strftime


class Homework(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100,  null=False)
    about = models.CharField(max_length=150,  null=False)
    content = models.TextField(max_length=512,  null=False)
    image = models.FileField(null=False, upload_to='upload/img')
    file = models.FileField(null=False, upload_to='upload/FilesHW')
    source = models.URLField(null=True)
