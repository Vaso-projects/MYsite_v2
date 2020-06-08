from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from time import strftime


class Groups(models.Model):
    name = models.CharField(max_length=128)


class Affiliation(models.Model):
    date_joined = models.DateField(null=True, blank=True, default=timezone.now)
    invite_reason = models.CharField(null=True, blank=True, max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, null=True, blank=True, on_delete=models.CASCADE)


class Homework(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    topic = models.CharField(max_length=100, help_text='Тема урока', null=False)
    about = models.CharField(max_length=100, help_text='Описание',  null=False)
    content = models.TextField(max_length=512, blank=True, help_text='Содержание', null=False)
    image = models.FileField(null=True, upload_to='upload/img', help_text='Описание')
    file = models.FileField(null=True, blank=True, upload_to='upload/FilesHW/')
    source = models.URLField(null=False, blank=True,)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

    def publish(self):
        self.published = timezone.now()
        self.save()


class Video(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/video_img')
    file = models.FileField(upload_to='upload/video')
    source = models.URLField(null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)


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
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)


class Source(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/url')
    source = models.URLField(null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)
