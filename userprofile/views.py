from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def user_profile(request):
    """ view for user profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'profile': profile,
    }

    return render(request, "userprofile/user_profile.html", context)
