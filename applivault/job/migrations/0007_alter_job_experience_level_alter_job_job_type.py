# Generated by Django 4.2.3 on 2023-09-15 21:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_job_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience_level',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Internship', 'Internship'), ('Entry Level', 'Entry Level'), ('Associate', 'Associate'), ('Mid-Senior Level', 'Mid-Senior Level'), ('Senior Level', 'Senior Level'), ('Director', 'Director'), ('Executive', 'Executive')], max_length=125),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')], max_length=125),
        ),
    ]
