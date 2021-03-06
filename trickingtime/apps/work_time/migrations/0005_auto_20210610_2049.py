# Generated by Django 3.2.4 on 2021-06-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_time', '0004_alter_workentry_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workentry',
            name='duration',
            field=models.TimeField(editable=False, help_text='The duration of time between begin and end', null=True, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='workentry',
            name='duration_decimal',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=3, null=True, verbose_name='Duration in Decimal'),
        ),
    ]
