# Generated by Django 3.0.5 on 2020-04-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0027_auto_20200428_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='t_description',
        ),
        migrations.AddField(
            model_name='service',
            name='service_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
