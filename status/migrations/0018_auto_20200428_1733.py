# Generated by Django 3.0.5 on 2020-04-28 21:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('status', '0017_auto_20200428_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status_class_design',
            new_name='class_design',
        ),
    ]
