from django.contrib import admin
from .models import Blood, Personal, ChronicDisease

class bloodAdmin(admin.ModelAdmin):
    class meta:
        model = Blood

admin.site.register(Blood, bloodAdmin)


class personalAdmin(admin.ModelAdmin):
    class meta:
        model = Personal

admin.site.register(Personal, personalAdmin)


class ChronicDiseaseAdmin(admin.ModelAdmin):
    class meta:
        model = ChronicDisease

admin.site.register(ChronicDisease, ChronicDiseaseAdmin)