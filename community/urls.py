from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.community, name="community"),
    path('recipes/', views.recipe_list, name='recipe'),
]
