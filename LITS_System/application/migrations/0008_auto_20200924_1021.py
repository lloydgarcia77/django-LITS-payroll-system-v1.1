# Generated by Django 2.2.3 on 2020-09-24 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20200923_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleaves',
            name='balance_as_of_this_date',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='employeeleaves',
            name='leave_credits',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='employeeleaves',
            name='less_this_application',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]