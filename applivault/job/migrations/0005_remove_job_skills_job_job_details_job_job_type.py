# Generated by Django 4.2.3 on 2023-09-15 20:55

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
        migrations.AddField(
            model_name='job',
            name='job_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')], default=django.utils.timezone.now, max_length=125),
            preserve_default=False,
        ),
    ]