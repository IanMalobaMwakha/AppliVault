# Generated by Django 4.2.3 on 2023-09-15 21:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_job_experience_level_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[['Remote', 'Remote'], ['On-site', 'On-site'], ['Hybrid', 'Hybrid']], max_length=125),
        ),
    ]
