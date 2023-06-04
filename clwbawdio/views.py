from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Clwb
from .forms import ClwbForm


def clwbawdio(request):
    """ A view to return the clwbawdio page """

    return render(request, 'clwbawdio/clwbawdio.html')


def faqs(request):
    """ A view to return the faqs page """

    return render(request, 'clwbawdio/faqs.html')

def clwbs(request):
    """ A view to return the clwbss page """

    return render(request, 'clwbawdio/clwbs.html')

def all_clwbs(request):
    """ A view to show all clwbs, including sorting and search queries """

    clwbs = clwb.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                clwbs = clwbs.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            clwbs =clwbs.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('clwbs'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            clwbs = clwbs.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'clwbs': clwbs,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'clwbawdio/clwbs.html', context)

@login_required
def add_clwb(request):
    """ Add a clwb to the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClwbForm(request.POST, request.FILES)
        if form.is_valid():
            clwb = form.save()
            messages.success(request, 'Successfully added clwb!')
            return redirect(reverse('clwbs', args=[clwb.id]))
        else:
            messages.error(
                request, 'Failed to add clwb. \
                Please ensure the form is valid.')
    else:
        form = ClwbForm()

    template = 'clwbs/add_clwb.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_clwb(request, clwb_id):
    """ Edit a clwb on the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    clwb = get_object_or_404(Clwb, pk=clwb_id)
    if request.method == 'POST':
        form = ClwbForm(request.POST, request.FILES, instance=clwb)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated clwb!')
            return redirect(reverse('clwb_detail', args=[clwb.id]))
        else:
            messages.error(request, 'Failed to update clwb. \
            Please ensure the form is valid.')
    else:
        form = ClwbForm(instance=clwb)
        messages.info(request, f'You are editing {clwb.name}')

    template = 'clwbs/edit_clwb.html'
    context = {
        'form': form,
        'clwb': clwb,
    }

    return render(request, template, context)


@login_required
def delete_clwb(request, clwb_id):
    """ Delete a clwb from the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    clwb = get_object_or_404(Clwb, pk=clwb_id)
    clwb.delete()
    messages.success(request, 'Clwb deleted!')
    return redirect(reverse('clwbs'))
