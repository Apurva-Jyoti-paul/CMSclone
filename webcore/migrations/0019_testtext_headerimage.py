# Generated by Django 3.2 on 2021-08-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0018_viewip'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtext',
            name='headerimage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]