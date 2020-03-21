from django.contrib import admin

from .models import Pet

# Allows the admin to see the Pet information from the model class


@admin.register(Pet)
# Tells the database how to display data
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
