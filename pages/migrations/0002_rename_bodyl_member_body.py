# Generated by Django 4.0.4 on 2022-04-19 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='bodyl',
            new_name='body',
        ),
    ]
