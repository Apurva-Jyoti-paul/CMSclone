# Generated by Django 3.2 on 2021-05-24 05:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0005_alter_text_block_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_block',
            name='cont',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='media'),
        ),
    ]
