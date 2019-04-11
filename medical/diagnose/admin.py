from django.contrib import admin
from .models import Diagnose, Schedule, Medication

class diagnoseAdmin(admin.ModelAdmin):
    class meta:
        model = Diagnose


admin.site.register(Diagnose, diagnoseAdmin)


class medicationAdmin(admin.ModelAdmin):
    class meta:
        model = Medication


admin.site.register(Medication, medicationAdmin)


class scheduleAdmin(admin.ModelAdmin):
    class meta:
        model = Schedule


admin.site.register(Schedule, scheduleAdmin)