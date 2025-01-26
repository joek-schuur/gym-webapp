from django.contrib import admin
from .models import MuscleGroup, Exercise

# class MuscleGroupAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

admin.site.register(MuscleGroup)
admin.site.register(Exercise)

