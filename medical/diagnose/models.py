from django.db import models
from profiles.models import Doctor, Patient

class Diagnose(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content[:20] + '...'
