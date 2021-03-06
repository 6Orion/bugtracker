# Generated by Django 2.2.6 on 2019-11-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='priority',
            field=models.CharField(choices=[('0', 'None'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High'), ('4', 'Urgent'), ('5', 'Immediate')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='bug',
            name='view_status',
            field=models.CharField(choices=[('1', 'Public'), ('0', 'Private')], default='1', max_length=1),
        ),
    ]
