# Generated by Django 3.2.9 on 2022-04-03 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
