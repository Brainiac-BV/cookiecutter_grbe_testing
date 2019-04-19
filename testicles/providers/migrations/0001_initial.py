# Generated by Django 2.0.13 on 2019-04-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('sub_service', models.CharField(blank=True, choices=[('Hair', (('braiding', 'braiding'), ('cut', 'cut'), ('w/d', 'Wash and dry'), ('styling', 'styling'))), ('Nails', (('natural', 'Natural Set'), ('full', 'Full Set'))), ('Make up', (('full_face', 'Full Face'), ('touchup', 'Touchup')))], max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
