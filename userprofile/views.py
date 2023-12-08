from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm


def user_profile(request):
    """ view for user profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    profile_form = ProfileForm(instance=profile)
    context = {
        'profile_form': profile_form,
    }

    return render(request, "userprofile/user_profile.html", context)
