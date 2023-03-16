from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Blog, Category
from .forms import BlogForm

# Create your views here.

def all_blogs(request):
    """ A view to show all blogs, including sorting and search queries """

    blogs = Blog.objects.all()
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
                blogs = blogs.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            blogs = blogs.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            blogs = blogs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('blogs'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            blogs = blogs.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'blogs': blogs,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'blogs/blogs.html', context)


def blog_detail(request, blog_id):
    """ A view to show individual blogs """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blogs/blog_detail.html', context)


@login_required
def add_blog(request):
    """ Add a blog to the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = BlogForm()
        
    template = 'blogs/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog on the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.name}')

    template = 'blogs/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a blog from the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blogs'))
