# Generated by Django 2.2.3 on 2020-02-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20200220_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='first_name',
            field=models.CharField(default='FN', max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='last_name',
            field=models.CharField(default='LN', max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='middle_name',
            field=models.CharField(default='MN', max_length=50),
        ),
    ]