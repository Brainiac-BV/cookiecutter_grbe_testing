# Generated by Django 2.0.13 on 2019-03-03 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_serviceprovider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='services_provided',
        ),
        migrations.DeleteModel(
            name='ServiceProvider',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
