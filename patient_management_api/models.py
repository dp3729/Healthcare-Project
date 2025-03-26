from django.db import models
from authentication_api.models import CustomUser  # Importing CustomUser for patient association

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="patient")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.phone}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    diagnosis = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.user.first_name} {self.patient.user.last_name}"
