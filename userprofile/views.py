from django.shortcuts import render
from .models import UserProfile


def user_profile(request):
    """ view for user profile """

    user_profile = UserProfile.objects.all()

    context = {
        'user_profile': user_profile,
    }

    return render(request, "userprofile/user_profile.html", context)
