from django.urls import path
from . import views


urlpatterns = [
    path('start', views.community, name="community"),
    path('recipe_posts/', views.recipe_list, name='recipes'),
    path('recipe_posts/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('workout_posts/', views.workout_list, name='workouts'),
    path('workout_posts/<slug:slug>/', views.workout_detail, name='workout_detail'),
    path('other_posts/', views.other_post_list, name='other_posts'),
    path('other_posts/<slug:slug>/',
         views.other_post_detail, name='other_post_detail'),
    path('user_posts', views.get_user_posts, name='user_posts'),
]
