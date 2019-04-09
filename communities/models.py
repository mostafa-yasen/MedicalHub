from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=60, default='Community Name', null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name