from django.shortcuts import render


def contact(request):
    """ view contact page """
    return render(request, 'contact/contact.html')
