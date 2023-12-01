from django.contrib import admin
from .models import Recipe, Workout, OtherPost

admin.site.register(Recipe)
admin.site.register(Workout)
admin.site.register(OtherPost)
