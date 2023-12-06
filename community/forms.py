from .models import Recipe, Workout, OtherPost
from django import forms


class RecipeForm(forms.ModelForm):
    """
    Class to make a new recipe post
    """
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients',
                  'instructions', 'recipe_type']
        labels = {
            'title': ('Title'),
            'description': ('Description'),
            'ingredients': ('Ingredients'),
            'instructions': ('Instructions'),
            'recipe_type': ('Type'),
        }


form = RecipeForm()
