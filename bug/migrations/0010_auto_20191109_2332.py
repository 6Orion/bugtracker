# Generated by Django 2.2.7 on 2019-11-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0009_auto_20191105_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='summary',
            field=models.CharField(max_length=120),
        ),
    ]
