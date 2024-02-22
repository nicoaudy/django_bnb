from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom user admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )

# Same implementation
# admin.site.register(models.User, CustomUserAdmin)
