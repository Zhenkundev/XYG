# Generated by Django 3.1.4 on 2022-03-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]