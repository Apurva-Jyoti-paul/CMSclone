# Generated by Django 3.2 on 2021-06-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0014_testtext_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtext',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
