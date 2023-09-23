from django.contrib import admin
from .models import Profile 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex', 'date_of_birth', ]
    raw_id_fields = ['user']