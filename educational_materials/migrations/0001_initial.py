# Generated by Django 3.0.6 on 2020-06-09 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default='2020-06-09 08:15')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=256)),
                ('image', models.FileField(upload_to='upload/video_img')),
                ('file', models.FileField(upload_to='upload/video')),
                ('source', models.URLField(null=True)),
                ('affiliation', models.ManyToManyField(to='educational_materials.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Textbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default='2020-06-09 08:15')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=256)),
                ('image', models.FileField(upload_to='upload/textbooks')),
                ('file', models.FileField(upload_to='upload/textbooks')),
                ('source', models.URLField(null=True)),
                ('affiliation', models.ManyToManyField(to='educational_materials.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default='2020-06-09 08:15')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=256)),
                ('image', models.FileField(upload_to='upload/url')),
                ('source', models.URLField(null=True)),
                ('affiliation', models.ManyToManyField(to='educational_materials.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default='2020-06-09 08:15')),
                ('topic', models.CharField(help_text='Тема урока', max_length=100)),
                ('about', models.CharField(help_text='Описание', max_length=100)),
                ('content', models.TextField(blank=True, help_text='Содержание', max_length=512)),
                ('image', models.FileField(help_text='Описание', null=True, upload_to='upload/img')),
                ('file', models.FileField(blank=True, null=True, upload_to='upload/FilesHW/')),
                ('source', models.URLField(blank=True)),
                ('group', models.ManyToManyField(to='educational_materials.Groups')),
                ('student', models.ManyToManyField(to='educational_materials.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default='2020-06-09 08:15')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=256)),
                ('file', models.FileField(upload_to='upload/audio')),
                ('source', models.URLField(null=True)),
                ('affiliation', models.ManyToManyField(to='educational_materials.Student')),
            ],
        ),
    ]
