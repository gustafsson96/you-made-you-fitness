from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Workout, OtherPost


def community(request):
    """ view start community page """
    return render(request, 'community/community.html')


def recipe_list(request):
    """ view to show recipe posts """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, "community/recipe_post_page.html", context)


def recipe_detail(request, slug, *args, **kwargs):
    if request.method == 'GET':
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=request.user.id).exists():
            liked = True

    context = {
            "recipe": recipe,
            "liked": liked,
    }

    return render(request, "community/recipe_post_detail_page.html", context)


def workout_list(request):
    """ view to show workout posts """

    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, "community/workout_post_page.html", context)


def workout_detail(request, slug, *args, **kwargs):
    if request.method == 'GET':
        queryset = Workout.objects.filter(status=1)
        workout = get_object_or_404(queryset, slug=slug)
        liked = False
        if workout.likes.filter(id=request.user.id).exists():
            liked = True

    context = {
            "workout": workout,
            "liked": liked,
    }

    return render(request, "community/workout_post_detail_page.html", context)


def other_post_list(request):
    """ view to show 'other' posts """

    other_posts = OtherPost.objects.all()

    context = {
        'other_posts': other_posts,
    }

    return render(request, "community/other_post_page.html", context)


def other_post_detail(request, slug, *args, **kwargs):
    if request.method == 'GET':
        queryset = OtherPost.objects.filter(status=1)
        other_post = get_object_or_404(queryset, slug=slug)
        liked = False
        if other_post.likes.filter(id=request.user.id).exists():
            liked = True

    context = {
            "other_post": other_post,
            "liked": liked,
    }

    return render(request, "community/other_post_detail_page.html", context)


def get_user_posts(request):
    """
    Get recipe posts specific to logged in user
    """
    user_recipes = Recipe.objects.filter(author=request.user)
    user_workouts = Workout.objects.filter(author=request.user)
    user_other_posts = OtherPost.objects.filter(author=request.user)

    context = {
        'user_recipes': user_recipes,
        'user_workouts': user_workouts,
        'user_other_posts': user_other_posts,
    }

    return render(request, 'community/logged_in_user_posts.html', context)
