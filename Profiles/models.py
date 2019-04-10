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
    avatar = models.ImageField(upload_to='avatars/', default='No Image')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField()
    age = models.PositiveSmallIntegerField(default=8)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(default='No BIO.')
    NID = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        if self.gender == 'M':
            return "Mr. %s %s" % (self.first_name, self.last_name)
        else:
            return "Mrs. %s %s" % (self.first_name, self.last_name)


class Doctor(models.Model):
    avatar = models.ImageField(upload_to='avatars/', default='No Image')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField()
    age = models.PositiveSmallIntegerField(default=22)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(default='No BIO.')
    specialization = models.CharField(max_length=50, choices=JOB_CHOICES)
    NID = models.CharField(max_length=14, null=False, blank=False)
    Job_ID = models.CharField(max_length=14, null=False, blank=False)
    rate = models.FloatField(default=0.0)

    def __str__(self):
        return "Dr. %s %s" % (self.first_name, self.last_name)