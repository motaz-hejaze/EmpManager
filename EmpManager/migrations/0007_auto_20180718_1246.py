# Generated by Django 2.0.7 on 2018-07-18 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManager', '0006_auto_20180717_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='salary',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
