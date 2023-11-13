from django.shortcuts import render


def home(request):
    """ view home page """
    return render(request, 'home/home.html')
