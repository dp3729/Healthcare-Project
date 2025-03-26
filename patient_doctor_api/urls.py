from django.urls import path
from .views import PatientDoctorListCreateView, PatientDoctorDetailView

urlpatterns = [
    path("patient-doctor/", PatientDoctorListCreateView.as_view(), name="patient-doctor-list"),
    path("patient-doctor/<int:pk>/", PatientDoctorDetailView.as_view(), name="patient-doctor-detail"),
]