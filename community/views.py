from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .models import Recipe, Workout, OtherPost
from userprofile.models import UserProfile
from .forms import RecipeForm, WorkoutForm, OtherPostForm


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
        queryset = Recipe.objects.all()
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
        queryset = Workout.objects.all()
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
        queryset = OtherPost.objects.all()
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
    get posts specific to logged in user
    """
    user_recipes = Recipe.objects.filter(author=request.user)
    user_workouts = Workout.objects.filter(author=request.user)
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
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.title)
            recipe_form.save()
            print("Recipe saved!")
            return redirect('user_posts')
        else:
            print("Error", recipe_form.errors)
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
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save(commit=False)
            workout.author = request.user
            workout.slug = slugify(workout.title)
            workout_form.save()
            print("Workout saved!")
            return redirect('user_posts')
        else:
            print("Error", workout_form.errors)
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
        other_post_form = OtherPostForm(request.POST)
        if other_post_form.is_valid():
            other_post = other_post_form.save(commit=False)
            other_post.author = UserProfile.objects.get(user=request.user)
            other_post.slug = slugify(other_post.title)
            other_post_form.save()
            print("Post saved!")
            return redirect('user_posts')
        else:
            print("Error", other_post_form.errors)
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
            print('Hello')
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
            print('Hello')
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
            print('Hello')
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
    return redirect('user_posts')


def delete_workout(workout, slug):
    """
    Delete an existing workout post
    """
    workout = get_object_or_404(Workout, slug=slug)
    workout.delete()
    return redirect('user_posts')


def delete_other_post(request, slug):
    """
    Delete an existing other post
    """
    other_post = get_object_or_404(OtherPost, slug=slug)
    other_post.delete()
    return redirect('user_posts')
