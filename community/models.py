from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))

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
    """ Model to post recipes """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    instructions = models.TextField(null=False, blank=False)
    recipe_type = models.CharField(
        max_length=50, choices=TYPE_OF_RECIPE, default='breakfast')
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Workout(models.Model):
    """ Model to post workouts """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='workout_post')
    updated_on = models.DateTimeField(auto_now=True)
    excercies = models.CharField(max_length=500, null=True, blank=True)
    instructions = models.TextField(null=False, blank=False)
    workout_type = models.CharField(
        max_length=50, choices=TYPE_OF_WORKOUT, default='cardio')
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='workout_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class OtherPost(models.Model):
    """ Model to make other posts """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='other_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='other_post_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
