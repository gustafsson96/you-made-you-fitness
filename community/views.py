from django.shortcuts import render
from django.views import generic
from .models import Recipe, Workout, OtherPost


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe_post_page.html'
    paginate_by = 5


class WorkoutList(generic.ListView):
    model = Workout
    queryset = Workout.objects.filter(status=1).order_by('-created_on')
    template_name = 'workout_post_page.html'
    paginate_by = 5


class OtherPostList(generic.ListView):
    model = OtherPost
    queryset = OtherPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'other_post_page.html'
    paginate_by = 5
