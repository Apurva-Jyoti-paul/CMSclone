# Generated by Django 3.2 on 2021-05-22 15:01

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=1000)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='webpage',
            fields=[
                ('title', models.CharField(default='untitled', max_length=200)),
                ('update', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('web', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcore.website')),
            ],
        ),
        migrations.CreateModel(
            name='text_block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=10000, null=True)),
                ('cont', cloudinary.models.CloudinaryField(max_length=255, verbose_name='media')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcore.webpage')),
            ],
        ),
    ]
