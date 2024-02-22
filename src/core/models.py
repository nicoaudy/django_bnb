from django.db import models


class TimestampedModel(models.Model):

    """ timestamped model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True     # Don't migrare this abstract model
