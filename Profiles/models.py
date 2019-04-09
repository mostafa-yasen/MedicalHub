from django.db import models

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

JOB_CHOICES = (
    ('cardiology', 'Cardiology'),
    ('orthopedics', 'Orthopedics'),
    ('general_surgery', 'General Surgery'),
    ('gastroenterologist', 'Gastroenterologist'),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField()
    age = models.IntegerField(default=8)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    NID = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        if self.gender == 'M':
            return "Mr. %s %s" % (self.first_name, self.last_name)
        else:
            return "Mr. %s %s" % (self.first_name, self.last_name)


class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField()
    age = models.IntegerField(default=22)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=50, choices=JOB_CHOICES)
    NID = models.CharField(max_length=14, null=False, blank=False)
    Job_ID = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        return "Dr. %s %s" % (self.first_name, self.last_name)