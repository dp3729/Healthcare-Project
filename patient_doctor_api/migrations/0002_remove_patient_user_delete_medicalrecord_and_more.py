# Generated by Django 5.1.7 on 2025-03-26 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patient_doctor_api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="user",
        ),
        migrations.DeleteModel(
            name="MedicalRecord",
        ),
        migrations.DeleteModel(
            name="Patient",
        ),
    ]
