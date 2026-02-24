from django.shortcuts import render
from .models import Patient, Doctor, Appointments
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer
from rest_framework import viewsets
# Create your views here.

class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class  = PatientSerializer


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer