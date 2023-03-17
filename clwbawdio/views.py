from django.shortcuts import render

def clwbawdio(request):
    """ A view to return the clwbawdio page """

    return render(request, 'clwbawdio/clwbawdio.html')


def faqs(request):
    """ A view to return the faqs page """

    return render(request, 'clwbawdio/faqs.html')