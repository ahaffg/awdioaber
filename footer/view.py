from django.shortcuts import render

def terms(request):
    """ A view to return the terms and conditions page page """

    return render(request, 'footer/terms.html')
