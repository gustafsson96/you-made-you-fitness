from django.shortcuts import render


def home(request):
    """ view home page """
    return render(request, 'home/home.html')


def custom_404(request, exception):
    """ view 404 page """
    return render(request, '404.html', status=404)
