from rest_framework import serializers
from .models import PatientDoctor

class PatientDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctor
        fields = ['id', 'patient', 'doctor', 'assigned_at']