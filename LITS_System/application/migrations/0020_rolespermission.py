# Generated by Django 3.1.2 on 2020-11-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0019_auto_20201027_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolesPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('immidiate_head', models.CharField(max_length=200)),
                ('employee_ci_rp_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_ci_rp_fk_r', to='application.companyinfo')),
            ],
        ),
    ]
