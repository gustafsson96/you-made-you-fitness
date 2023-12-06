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


class WorkoutForm(forms.ModelForm):
    """
    Class to make a new reservation
    """
    class Meta:
        model = Workout
        fields = ['name', 'date', 'time', 'number_of_guests', 'message']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date', 'placeholder': 'yyyy-mm-dd'}
            )}
        labels = {
            'name': ('Name'),
            'date': ('Date'),
            'time': ('Time'),
            'number_of_guests': ('Number of Guests'),
            'message': ('Special Requests or Allergy Information? Add here!'),
        }


form = WorkoutForm()


class OtherPostForm(forms.ModelForm):
    """
    Class to make a new reservation
    """
    class Meta:
        model = OtherPost
        fields = ['name', 'date', 'time', 'number_of_guests', 'message']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date', 'placeholder': 'yyyy-mm-dd'}
            )}
        labels = {
            'name': ('Name'),
            'date': ('Date'),
            'time': ('Time'),
            'number_of_guests': ('Number of Guests'),
            'message': ('Special Requests or Allergy Information? Add here!'),
        }


form = OtherPostForm()
