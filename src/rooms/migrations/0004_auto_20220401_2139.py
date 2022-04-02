# Generated by Django 3.2.9 on 2022-04-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20220401_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalroom',
            name='code',
            field=models.TextField(default=0, verbose_name='Code'),
        ),
        migrations.AddField(
            model_name='historicalroom',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='discount'),
        ),
        migrations.AddField(
            model_name='historicalroom',
            name='photo',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='code',
            field=models.TextField(default=0, verbose_name='Code'),
        ),
        migrations.AddField(
            model_name='room',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='discount'),
        ),
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.ImageField(null=True, upload_to='rooms'),
        ),
        migrations.AlterField(
            model_name='historicalroom',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='historicalroom',
            name='type',
            field=models.CharField(choices=[('Habitacion Simple', 'Simple'), ('Habitacion doble', 'Double'), ('Habitacion Matrimonial', 'Suite'), ('Especial', 'Special')], max_length=40, verbose_name='Room Type'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('Habitacion Simple', 'Simple'), ('Habitacion doble', 'Double'), ('Habitacion Matrimonial', 'Suite'), ('Especial', 'Special')], max_length=40, verbose_name='Room Type'),
        ),
    ]
