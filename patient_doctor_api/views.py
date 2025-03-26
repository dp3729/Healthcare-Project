from django.shortcuts import render
from rest_framework import generics, permissions
from .models import PatientDoctor
from .serializers import PatientDoctorSerializer

# Create your views here.

class PatientDoctorListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctor.objects.all()
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class PatientDoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDoctor.objects.all()
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
