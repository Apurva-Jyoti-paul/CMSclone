# Generated by Django 3.2 on 2021-05-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0007_alter_text_block_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='text_block',
            name='link',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
