from django.contrib import admin
from .models import Profile 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex', 'phone_number', 'date_of_birth', 'photo', ]
    raw_id_fields = ['user']