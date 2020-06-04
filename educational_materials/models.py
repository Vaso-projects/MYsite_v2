from django.db import models
from time import strftime


class Homework(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))
    title = models.CharField(max_length=100,  null=False)
    about = models.CharField(max_length=100,  null=False)
    content = models.TextField(max_length=512,  null=False)
    image = models.FileField(null=False, upload_to='upload/img')
    file = models.FileField(null=False, upload_to='upload/FilesHW')
    source = models.URLField(null=True)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UploadHomework(models.Model):
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M'))

    # file = models.FileField(null=False, upload_to='upload/UsersHW/{{login}}/%Y/%m/%d/')
    file = models.FileField(upload_to=user_directory_path)


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
