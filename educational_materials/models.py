from django.db import models
from time import strftime


class Homework(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100,  null=False)
    content = models.TextField(max_length=512,  null=False)
    image = models.FileField(null=False, upload_to='upload/img')
    file = models.FileField(null=False, upload_to='upload/FilesHW')
    source = models.URLField(null=True)


class Video(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/video_img')
    file = models.FileField(upload_to='upload/video')
    source = models.URLField(null=True)


class Audio(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    file = models.FileField(upload_to='upload/audio')
    source = models.URLField(null=True)


class Textbooks(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/textbooks')
    file = models.FileField(upload_to='upload/textbooks')
    source = models.URLField(null=True)


class Source(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/url')
    source = models.URLField(null=True)
