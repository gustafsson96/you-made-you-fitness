from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.community, name="community"),
    path('recipe_posts/', views.recipe_list, name='recipe'),
    path('workout_posts/', views.workout_list, name='workout'),
    path('other_posts/', views.other_post_list, name='other'),
]
