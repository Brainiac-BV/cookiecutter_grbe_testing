# Generated by Django 2.0.13 on 2019-03-02 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_is_service_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_services', models.CharField(max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_service_provider',
            new_name='service_provider_status',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='services_provided',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='services_provided',
            field=models.ManyToManyField(help_text='select the services you would like to provide', to='users.Services'),
        ),
    ]