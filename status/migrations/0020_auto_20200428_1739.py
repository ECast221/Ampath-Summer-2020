# Generated by Django 3.0.5 on 2020-04-28 21:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('status', '0019_auto_20200428_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status_category_color',
            new_name='color_name',
        ),
    ]
