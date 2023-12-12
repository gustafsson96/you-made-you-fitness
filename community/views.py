from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Workout, OtherPost
from userprofile.models import UserProfile
from .forms import RecipeForm, WorkoutForm, OtherPostForm
from django.utils.text import slugify
from django.contrib import messages


def community(request):
    """ view start community page """
    return render(request, 'community/community.html')


def community_unauthorized(request):
    """ view community page for unauthorized users """
    return render(request, 'community/community_unauthorized.html')


def recipe_list(request):
    """ view to show recipe posts """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, "community/recipe_post_page.html", context)


def recipe_detail(request, slug, *args, **kwargs):
    if request.method == 'GET':
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)

    context = {
        "recipe": recipe,
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
        queryset = Workout.objects.all()
        workout = get_object_or_404(queryset, slug=slug)

    context = {
        "workout": workout,
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
        queryset = OtherPost.objects.all()
        other_post = get_object_or_404(queryset, slug=slug)

    context = {
        "other_post": other_post,
    }

    return render(request, "community/other_post_detail_page.html", context)


def get_user_posts(request):
    """
    get posts specific to logged in user
    """
    user_recipes = Recipe.objects.filter(author__user=request.user)
    user_workouts = Workout.objects.filter(author__user=request.user)
    user_other_posts = OtherPost.objects.filter(author__user=request.user)

    context = {
        'user_recipes': user_recipes,
        'user_workouts': user_workouts,
        'user_other_posts': user_other_posts,
    }

    return render(request, 'community/logged_in_user_posts.html', context)


def add_recipe_post(request):
    """
    Create and validate a new recipe post
    """
    if request.method == 'POST':
        show_image_field = False
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = UserProfile.objects.get(user=request.user)
            recipe.slug = slugify(recipe.title)
            recipe_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your recipe post has been created')
            return redirect('recipes')
    else:
        recipe_form = RecipeForm()

    context = {
        'recipe_form': recipe_form,
    }

    return render(request, 'community/add_recipe_post.html', context)


def add_workout_post(request):
    """
    Create and validate a new workout post
    """
    if request.method == 'POST':
        show_image_field = False
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save(commit=False)
            workout.author = UserProfile.objects.get(user=request.user)
            workout.slug = slugify(workout.title)
            workout_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your workout post has been created')
            return redirect('workouts')
    else:
        workout_form = WorkoutForm()

    context = {
        'workout_form': workout_form,
    }

    return render(request, 'community/add_workout_post.html', context)


def add_other_post(request):
    """
    Create and validate a new other post
    """
    if request.method == 'POST':
        show_image_field = False
        other_post_form = OtherPostForm(request.POST)
        if other_post_form.is_valid():
            other_post = other_post_form.save(commit=False)
            other_post.author = UserProfile.objects.get(user=request.user)
            other_post.slug = slugify(other_post.title)
            other_post_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your post has been created')
            return redirect('other_posts')
    else:
        other_post_form = OtherPostForm()

    context = {
        'other_post_form': other_post_form,
    }

    return render(request, 'community/add_other_post.html', context)


def edit_recipe_post(request, slug, *args, **kwargs):
    """ view to edit a recipe post """

    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your recipe post was updated successfully')
            return redirect('user_posts')
    else:
        recipe_form = RecipeForm(instance=recipe)

    context = {
        'recipe_form': recipe_form,
        'recipe': recipe,
    }

    return render(request, 'community/edit_recipe_post.html', context)


def edit_workout_post(request, slug, *args, **kwargs):
    """ view to edit a workout post """

    workout = get_object_or_404(Workout, slug=slug)

    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST, instance=workout)
        if workout_form.is_valid():
            workout_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your workout post was updated successfully')
            return redirect('user_posts')
    else:
        workout_form = WorkoutForm(instance=workout)

    context = {
        'workout_form': workout_form,
        'workout': workout,
    }

    return render(request, 'community/edit_workout_post.html', context)


def edit_other_post(request, slug, *args, **kwargs):
    """ view to edit other posts """

    other_post = get_object_or_404(OtherPost, slug=slug)

    if request.method == 'POST':
        other_post_form = OtherPostForm(request.POST, instance=other_post)
        if other_post_form.is_valid():
            other_post_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your post was updated successfully')
            return redirect('user_posts')
    else:
        other_post_form = OtherPostForm(instance=other_post)

    context = {
        'other_post_form': other_post_form,
        'other_post_form': other_post_form,
    }

    return render(request, 'community/edit_other_post.html', context)


def delete_recipe(request, slug):
    """
    Delete an existing recipe post
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.delete()
    messages.add_message(request, messages.ERROR,
                         'Your recipe post has been deleted')
    return redirect('user_posts')


def delete_workout(workout, slug):
    """
    Delete an existing workout post
    """
    workout = get_object_or_404(Workout, slug=slug)
    workout.delete()
    messages.add_message(request, messages.ERROR,
                         'Your workout post has been deleted')
    return redirect('user_posts')


def delete_other_post(request, slug):
    """
    Delete an existing other post
    """
    other_post = get_object_or_404(OtherPost, slug=slug)
    other_post.delete()
    messages.add_message(request, messages.ERROR,
                         'Your post has been deleted')
    return redirect('user_posts')


def community_search_result(request):
    """ a view for searching posts """
    if request.GET:
        if 'q' in request.GET:
            query = request.GET.get('q', '')

        recipes = Recipe.objects.filter(
            title__icontains=query) | Recipe.objects.filter(
                ingredients__icontains=query)
        workouts = Workout.objects.filter(
            title__icontains=query) | Workout.objects.filter(
                instructions__icontains=query)
        other_posts = OtherPost.objects.filter(
            title__icontains=query) | OtherPost.objects.filter(
                content__icontains=query)

    context = {
        'query': query,
        'recipes': recipes,
        'workouts': workouts,
        'other_posts': other_posts,
    }

    return render(request, 'community/search_results.html', context)
