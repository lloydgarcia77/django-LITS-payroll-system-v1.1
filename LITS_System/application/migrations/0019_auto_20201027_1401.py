# Generated by Django 2.2.3 on 2020-10-27 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_auto_20201027_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeepayroll',
            old_name='late_undertime_min',
            new_name='late_undertime_min_amount',
        ),
    ]
