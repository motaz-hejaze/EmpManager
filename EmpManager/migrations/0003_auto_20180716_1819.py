# Generated by Django 2.0.7 on 2018-07-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManager', '0002_auto_20180716_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='default_deduction',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='position',
            name='main_salary_max',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='position',
            name='main_salary_min',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salary',
            name='deductions',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salary',
            name='earnings',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salary',
            name='main_salary',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
