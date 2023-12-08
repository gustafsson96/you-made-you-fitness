from django.shortcuts import render
from .models import UserProfile


def user_profile(request):
    """ view for user profile """

    profile = UserProfile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, "userprofile/user_profile.html", context)
