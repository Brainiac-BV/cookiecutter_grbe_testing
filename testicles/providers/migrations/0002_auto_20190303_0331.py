# Generated by Django 2.0.13 on 2019-03-03 03:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='user_info',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='user_info',
            field=models.ForeignKey(blank=True, null=True, on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]
