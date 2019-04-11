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


class Medication(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField(default="Noting.")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    notes = models.TextField()
    time = models.TimeField()

    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.medication.name + " - " + str(self.time)
        # return "%s | %s:%s" % (self.medication, self.time.hour, self.time.minute)