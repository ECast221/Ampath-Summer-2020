# Generated by Django 3.0.5 on 2020-04-28 21:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('status', '0020_auto_20200428_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status_category_tag',
            new_name='tag',
        ),
    ]
