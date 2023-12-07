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
    path("add_recipe", views.add_recipe_post, name="add_recipe"),
    path("add_workout", views.add_workout_post, name="add_workout"),
    path("add_other", views.add_other_post, name="add_other"),
    path('edit_recipe/<slug:slug>/', views.edit_recipe_post, name="edit_recipe"),
    path('edit_workout/<slug:slug>/', views.edit_workout_post, name="edit_workout"),
    path('edit_other_post/<slug:slug>/', views.edit_other_post, name="edit_other_post"),
    path('delete_recipe/<slug:slug>/',
         views.delete_recipe, name="delete_recipe"),
    path('delete_workout/<slug:slug>/',
         views.delete_workout, name="delete_workout"),
]
