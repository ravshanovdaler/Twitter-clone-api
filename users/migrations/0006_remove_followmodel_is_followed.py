# Generated by Django 4.2.5 on 2023-09-24 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_followmodel_is_followed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followmodel',
            name='is_followed',
        ),
    ]
