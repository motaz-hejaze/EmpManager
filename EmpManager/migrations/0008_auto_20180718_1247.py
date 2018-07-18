# Generated by Django 2.0.7 on 2018-07-18 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManager', '0007_auto_20180718_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='position',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='position',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sibling',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sibling',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]