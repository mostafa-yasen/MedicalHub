from django.contrib import admin
from .models import Patient, Doctor


class patientAdmin(admin.ModelAdmin):
    class Meta:
        model = Patient


admin.site.register(Patient, patientAdmin)



class doctorAdmin(admin.ModelAdmin):
    class Meta:
        model = Doctor


admin.site.register(Doctor, doctorAdmin)