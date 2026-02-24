from django.shortcuts import render
from .models import Patient, Doctor, Appointments
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.

class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class  = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['phone', 'created_at']
    search_fields = ['name', 'phone']
    ordering_fields = ['created_at', 'name']


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer