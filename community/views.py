from django.shortcuts import render, redirect
from .models import Recipe, Workout, OtherPost


def community(request):
    """ view start community page """
    return render(request, 'community/community.html')


def recipe_list(request):
    """ A view to show recipe posts """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, "community/recipe_post_page.html", context)


def workout_list(request):
    """ A view to show workout posts """

    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, "community/workout_post_page.html", context)


def other_post_list(request):
    """ A view to show other posts """

    other_posts = OtherPost.objects.all()

    context = {
        'other_posts': other_posts,
    }

    return render(request, "community/other_post_page.html", context)
