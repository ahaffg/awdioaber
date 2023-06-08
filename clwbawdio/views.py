from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower


def clwbawdio(request):
    """ A view to return the clwbawdio page """

    return render(request, 'clwbawdio/clwbawdio.html')


def faqs(request):
    """ A view to return the faqs page """

    return render(request, 'clwbawdio/faqs.html')
