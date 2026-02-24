from django.contrib import admin

from .models import Appointments, Doctor, Patient, Patient
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointments)