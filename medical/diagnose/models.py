from django.db import models
from profiles.models import Doctor, Patient
from datetime import datetime

class Diagnose(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content[: 20] + ' ...'
