from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Replay, Category
from .forms import ReplayForm

# Create your views here.


def all_replays(request):
    """ A view to show all replays, including sorting and search queries """

    replays = Replay.objects.all()
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
                replays = replays.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            replays = replays.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            replays = replays.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('replays'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            replays = replays.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'replays': replays,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'replay/replays.html', context)


def replay_detail(request, replay_id):
    """ A view to show individual replay details """

    replay = get_object_or_404(Replay, pk=replay_id)

    context = {
        'replay': replay,
    }

    return render(request, 'replays/replay_detail.html', context)


@login_required
def add_replay(request):
    """ Add a replay to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReplayForm(request.POST, request.FILES)
        if form.is_valid():
            replay = form.save()
            messages.success(request, 'Successfully added replay!')
            return redirect(reverse('replay_detail', args=[replay.id]))
        else:
            messages.error(
                request, 'Failed to add replay. \
                    Please ensure the form is valid.')
    else:
        form = ReplayForm()

    template = 'replay/add_replay.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_replay(request, replay_id):
    """ Edit a replay in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    replay = get_object_or_404(Replay, pk=replay_id)
    if request.method == 'POST':
        form = ReplayForm(request.POST, request.FILES, instance=replay)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated replay!')
            return redirect(reverse('replay_detail', args=[replay.id]))
        else:
            messages.error(
                request, 'Failed to update replay. \
                    Please ensure the form is valid.')
    else:
        form = ReplayForm(instance=replay)
        messages.info(request, f'You are editing {replay.name}')

    template = 'replay/edit_replay.html'
    context = {
        'form': form,
        'replay': replay,
    }

    return render(request, template, context)


@login_required
def delete_replay(request, replay_id):
    """ Delete a replay from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    replay = get_object_or_404(Replay, pk=replay_id)
    replay.delete()
    messages.success(request, 'Replay deleted!')
    return redirect(reverse('replay'))
