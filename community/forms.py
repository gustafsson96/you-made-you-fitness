from .models import Recipe, Workout, OtherPost
from django import forms


class RecipeForm(forms.ModelForm):
    """
    Class to make a new recipe post
    """
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'description', 'ingredients',
                  'instructions', 'recipe_type', 'recipe_image']
        labels = {
            'title': ('Title'),
            'description': ('Description'),
            'ingredients': ('Ingredients'),
            'instructions': ('Instructions'),
            'recipe_type': ('Type'),
        }


form = RecipeForm()


class WorkoutForm(forms.ModelForm):
    """
    Class to make a new workout post
    """
    class Meta:
        model = Workout
        fields = ['title', 'slug', 'equipment', 'exercises',
                  'instructions', 'workout_type', 'image']
        labels = {
            'title': ('Title'),
            'equipment': ('Equipment'),
            'exercises': ('Exercises'),
            'instructions': ('Instructions'),
            'workout_type': ('Type'),
        }


form = WorkoutForm()


class OtherPostForm(forms.ModelForm):
    """
    Class to make a new other post
    """
    class Meta:
        model = OtherPost
        fields = ['title', 'slug', 'content', 'image']
        labels = {
            'title': ('Title'),
            'content': ('Content'),
        }


form = OtherPostForm()
