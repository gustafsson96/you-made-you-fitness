from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from userprofile.models import UserProfile

TYPE_OF_RECIPE = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('snack', 'Snack'),
    ('other', 'Other'),
)

TYPE_OF_WORKOUT = (
    ('cardio', 'Cardio'),
    ('strength', 'Strength'),
    ('hiit', 'HIIT'),
    ('yoga', 'Yoga'),
    ('stretch', 'Stretch'),
    ('other', 'Other'),
)


class Recipe(models.Model):
    """ model to post recipes """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    instructions = models.TextField(null=False, blank=False)
    recipe_type = models.CharField(
        max_length=50, choices=TYPE_OF_RECIPE, default='breakfast')
    recipe_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Workout(models.Model):
    """ model to post workouts """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    equipment = models.CharField(max_length=500, null=True, blank=True)
    exercises = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=False, blank=False)
    workout_type = models.CharField(
        max_length=50, choices=TYPE_OF_WORKOUT, default='cardio')
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class OtherPost(models.Model):
    """ model to make other posts """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
