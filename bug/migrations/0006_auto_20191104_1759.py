# Generated by Django 2.2.6 on 2019-11-04 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('bug', '0005_auto_20191103_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='project.Project'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_authors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='resolution',
            field=models.CharField(choices=[('0', 'Open'), ('1', 'Reopened'), ('2', 'Unable to reproduce'), ('3', 'Closed'), ('4', 'Suspended')], default='0', max_length=1),
        ),
    ]