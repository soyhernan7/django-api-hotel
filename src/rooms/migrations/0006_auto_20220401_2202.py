# Generated by Django 3.2.9 on 2022-04-02 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220401_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalroom',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='room',
            name='discount',
        ),
        migrations.AddField(
            model_name='historicalroom',
            name='discount_rate',
            field=models.PositiveIntegerField(default=0, verbose_name='Discount Rate'),
        ),
        migrations.AddField(
            model_name='room',
            name='discount_rate',
            field=models.PositiveIntegerField(default=0, verbose_name='Discount Rate'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]