from django.shortcuts import render


def home(request):
    """ view home page """
    return render(request, 'home/home.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
