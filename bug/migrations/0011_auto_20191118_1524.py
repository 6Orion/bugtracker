# Generated by Django 2.2.7 on 2019-11-18 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0010_auto_20191109_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to_bugs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_of_bugs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_bugs', to='project.Project'),
        ),
    ]