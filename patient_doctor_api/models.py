from django.db import models
from authentication_api.models import CustomUser
from patient_management_api.models import Patient
from doctor_management_api.models import Doctor

# Create your models here.

class PatientDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="assigned_doctors")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patients")
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"