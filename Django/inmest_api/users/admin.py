from django.contrib import admin
from .models import IMUser, Cohort, CohortMember

# Register your models here.

# This code registers three models (IMUser, Cohort, CohortMember) in the admin interface.
# It uses the @admin.register decorator for model registration, which is a common approach in Django.
    # If you need extensive customization for an admin interface, method 1 with separate admin classes might be more manageable.
    # For smaller projects or simple admin displays, method 2 might be sufficient.
    # Consistency within your project is essential, so choose the approach that aligns best with your coding style and team conventions.
    # The custom admin classes are currently empty, leaving room for future admin interface customizations.
    
    # METHOD 1
@admin.register(IMUser)
class IMUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user_type", "date_created")

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display=("name", "year", "author", "date_created")

@admin.register(CohortMember)
class CohortMemberAdmin(admin.ModelAdmin):
    list_display=("cohort", "member", "date_created")

    # METHOD 2
# class IMUserAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name", "user_type", "date_created")

# class CohortAdmin(admin.ModelAdmin):
#     list_display=("name", "year", "author", "date_created")

# class CohortMemberAdmin(admin.ModelAdmin):
#     list_display=("cohort", "member", "date_created")

# admin.site.register(IMUser)
# admin.site.register(Cohort)
# admin.site.register(CohortMember)