from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone
from time import strftime


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Groups(models.Model):
    name = models.OneToOneField(Group, on_delete=models.CASCADE)


class Homework(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    topic = models.CharField(max_length=100, help_text='Тема урока', null=False)
    about = models.CharField(max_length=100, help_text='Описание',  null=False)
    content = models.TextField(max_length=512, blank=True, help_text='Содержание', null=False)
    image = models.FileField(null=True, upload_to=None)
    file = models.FileField(null=True, blank=True, upload_to='upload/FilesHW/')
    source = models.URLField(null=False, blank=True,)
    student = models.ManyToManyField(Student)
    group = models.ManyToManyField(Groups)

    def publish(self):
        self.published = timezone.now()
        self.save()


class Video(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to=None)
    file = models.FileField(null=False, blank=True, upload_to='upload/video')
    source = models.URLField(null=True)
    student = models.ManyToManyField(Student)


class Audio(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    file = models.FileField(upload_to='upload/audio')
    source = models.URLField(null=True)
    student = models.ManyToManyField(Student)


class Textbooks(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/textbooks')
    file = models.FileField(upload_to='upload/textbooks')
    source = models.URLField(null=True)
    student = models.ManyToManyField(Student)


class Source(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    image = models.FileField(upload_to='upload/url')
    source = models.URLField(null=True)
    student = models.ManyToManyField(Student)

