# Generated by Django 3.2 on 2021-06-13 15:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0011_alter_contents_align'),
    ]

    operations = [
        migrations.CreateModel(
            name='testtext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
