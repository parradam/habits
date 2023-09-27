from django.contrib import admin
from .models import HabitUnit, HabitType, HabitStatus, HabitEntry, HabitTarget

# Register your models here.
admin.site.register(HabitUnit)
admin.site.register(HabitType)
admin.site.register(HabitStatus)
admin.site.register(HabitEntry)
admin.site.register(HabitTarget)
