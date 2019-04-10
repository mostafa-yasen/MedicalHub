from django.contrib import admin
from .models import Diagnose

class diagnoseAdmin(admin.ModelAdmin):
    def meta(self):
        model = Diagnose


admin.site.register(Diagnose, diagnoseAdmin)