from django.shortcuts import render, redirect
from .models import Recipe, Workout, OtherPost


def community(request):
    """ view start community page """
    return render(request, 'community/community.html')


def recipe_list(request):
    """ A view to show all workout guides """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, "community/recipe_post_page.html", context)


## class WorkoutList(generic.ListView):
##    model = Workout
##    queryset = Workout.objects.filter(status=1).order_by('-created_on')
##    template_name = 'workout_post_page.html'
##    paginate_by = 5


## class OtherPostList(generic.ListView):
##     model = OtherPost
##    queryset = OtherPost.objects.filter(status=1).order_by('-created_on')
##    template_name = 'other_post_page.html'
##   paginate_by = 5
