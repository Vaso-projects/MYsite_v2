# Generated by Django 3.0.6 on 2020-05-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_materials', '0005_auto_20200530_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='published',
            field=models.DateTimeField(default='2020-05-30 13:34'),
        ),
    ]