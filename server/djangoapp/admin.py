from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1  # Number of empty CarModel forms to display in CarMake admin


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'year', 'car_make']
    list_filter = ['type', 'year', 'car_make']
    search_fields = ['name', 'car_make__name']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
