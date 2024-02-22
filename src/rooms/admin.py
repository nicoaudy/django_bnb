from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country",
                        "city", "address", "price", "room_type")}
        ),
        (

            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (

            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")}
        ),
        (

            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            }
        ),
        (

            "Last Details",
            {"fields": ("host",)}
        ),
    )

    list_display = (
        "host",
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "total_amenities"
    )

    ordering = ("name", "price")

    list_filter = (
        "instant_book",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def total_amenities(self, obj):
        return obj.amenities.count()


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ item admin definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ photo admin definition """

    pass
