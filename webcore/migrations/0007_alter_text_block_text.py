# Generated by Django 3.2 on 2021-05-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0006_alter_text_block_cont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_block',
            name='text',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
