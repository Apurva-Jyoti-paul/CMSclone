# Generated by Django 3.2 on 2021-06-19 18:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0015_testtext_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtext',
            name='text2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
