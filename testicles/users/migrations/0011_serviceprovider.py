# Generated by Django 2.0.13 on 2019-03-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190303_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_provided', models.ManyToManyField(help_text='select the services you would like to provide', to='users.Services')),
            ],
        ),
    ]
