from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user'),

        fields = ['bio', 'fun_fact', 'profile_picture']
        placeholders = {
            'bio': 'Bio',
            'fun_fact': 'Fun Fact',
            'profile_picture': 'Profile Picture',
        }


form = ProfileForm()
