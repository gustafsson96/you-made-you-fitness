from django.urls import path
from . import views


urlpatterns = [
    path('start', views.community, name="community"),
    path('recipe_posts/', views.recipe_list, name='recipes'),
    path('workout_posts/', views.workout_list, name='workouts'),
    path('other_posts/', views.other_post_list, name='other_posts'),
]
