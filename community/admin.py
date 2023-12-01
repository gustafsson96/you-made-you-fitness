from django.contrib import admin
from .models import Recipe, Workout, OtherPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdminRecipe(SummernoteModelAdmin):

    summernote_fields = ('instructions')


@admin.register(Workout)
class PostAdminWorkout(SummernoteModelAdmin):

    summernote_fields = ('instructions')


@admin.register(OtherPost)
class PostAdminOther(SummernoteModelAdmin):

    summernote_fields = ('content')
