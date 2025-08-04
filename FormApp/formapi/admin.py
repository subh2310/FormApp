from django.contrib import admin
from formapi.models import Profile


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city',
                    'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']
