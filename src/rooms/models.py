from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimestampedModel):

    """ abstract item model """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    pass


class Room(core_models.TimestampedModel):

    """ Room model definition """

    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = models.CharField(max_length=200, null=True, choices=[
                               ('', 'Select Country')] + CountryField().choices)
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True,)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
