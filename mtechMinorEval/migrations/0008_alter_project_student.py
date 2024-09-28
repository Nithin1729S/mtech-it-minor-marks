# Generated by Django 5.1 on 2024-09-28 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtechMinorEval', '0007_alter_projectevalsummary_examiner_name_and_more'),
        ('users', '0004_student_cgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='users.student'),
        ),
    ]