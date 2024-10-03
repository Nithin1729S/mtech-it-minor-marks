# Generated by Django 5.1 on 2024-10-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtechMinorEval', '0014_pathaccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathaccess',
            name='bounces',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pathaccess',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pathaccess',
            name='path',
            field=models.CharField(max_length=255),
        ),
    ]