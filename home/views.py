from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')


def policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/policy.html')


def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms.html')


def construction(request):
    """ A view to return the construction page """

    return render(request, 'home/construction.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')
