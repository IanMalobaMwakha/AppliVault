# Generated by Django 4.2.3 on 2023-09-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(blank=True, to='job.job'),
        ),
    ]