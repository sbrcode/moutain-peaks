# Generated by Django 3.1.7 on 2021-04-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peaks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peaklocation',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='peaklocation',
            name='lon',
            field=models.FloatField(default=0),
        ),
    ]
