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

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    class Meta:
        verbose_name_plural = "House Rule"


class Room(core_models.TimestampedModel):

    """ Room model definition """

    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE)
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
        RoomType, related_name="room_types", on_delete=models.SET_NULL, null=True,)
    amenities = models.ManyToManyField(
        Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(
        Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()

        return all_ratings / len(all_reviews)


class Photo(core_models.TimestampedModel):

    """ Photo model definition"""
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(
        Room, related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
