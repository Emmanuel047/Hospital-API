from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    address = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 15)
    Gender = models.Choices("male", "female", "other")
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'patient')

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    Full_name = models.CharField(max_length = 30)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length = 20)
    specialization = models.CharField(max_length=15)
    registration_no = models.CharField(unique = True)
    available_days = models.JSONField(default = list)
    slot_duration = models.IntegerField(default = 30)

    def __str__(self):
        return f"Dr, {self.Full_name} - {self.specialization}"
    
class Appointments(models.Model):
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name = 'doctor')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
        ('completed', 'completed'),
        ('scheduled','Scheduled'),
    ]
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'scheduled')
    appointment_no = models.CharField(max_length = 50, editable = False)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    appointment_time = models.TimeField()

    class Meta:
        unique_together = ['appointment_no', 'appointment_time', 'doctor']

    def __str__(self):
        return f"Appointment for {self.patients.name} with Dr.{self.doctor.Full_name}"