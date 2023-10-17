# Generated by Django 4.2.5 on 2023-10-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Temp', 'Temp')], max_length=15),
        ),
    ]
