# Generated by Django 3.2 on 2021-05-24 04:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0003_text_block_align'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_block',
            name='cont',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='media'),
        ),
    ]
