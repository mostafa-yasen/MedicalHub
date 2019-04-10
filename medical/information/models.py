from django.db import models
from profiles.models import Doctor, Patient

class Blood(models.Model):
    TYPE_CHOICES = (
        ("A", "A"),
        ("O", "O"),
        ("B", "B"),
        ("B-", "B-"),
        ("O-", "O-"),
        ("O+", "O+")
    )

    carbon_dioxide = models.CharField(max_length=20)
    glucose = models.CharField(max_length=20)
    hormones = models.CharField(max_length=20)
    proteins = models.CharField(max_length=20)
    mineral_salts = models.CharField(max_length=20)
    fats = models.CharField(max_length=20)
    typt = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.type


class Personal(models.Model):
    COLOR_TYPES = (
        ("Very Light","Very Light"),
        ("Normal Light","Normal Light"),
        ("Medium","Medium"),
        ("Light Brown","Light Brown"),
        ("Medium Brown","Medium Brown"),
        ("Brown","Brown"),
    )

    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    skin_color = models.CharField(max_length=20, choices=COLOR_TYPES)

    def __str__(self):
        return "%s kg - %s cm" % (self.weight, self.height)


class ChronicDisease(models.Model):
    name = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.name