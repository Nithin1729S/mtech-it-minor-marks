# Generated by Django 5.1 on 2024-08-31 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtechMinorEval', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examinerevaluation',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='examinerevaluation',
            name='evaluated_at',
        ),
        migrations.RemoveField(
            model_name='guideevaluation',
            name='evaluated_at',
        ),
        migrations.AddField(
            model_name='examinerevaluation',
            name='datetime_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examinerevaluation',
            name='datetime_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guideevaluation',
            name='datetime_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guideevaluation',
            name='datetime_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examinerevaluation',
            name='depthOfUnderstanding',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='examinerevaluation',
            name='presentation',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='examinerevaluation',
            name='report',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='examinerevaluation',
            name='vivaVoce',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='examinerevaluation',
            name='workDoneAndResults',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)]),
        ),
    ]