from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Blog_category
from .forms import ProductForm

# Create your views here.


def all_posts(request):
    """ A view to show all posts, including sorting and search queries """

    posts = Post.objects.all()
    query = None
    blog_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                posts = posts.annotate(lower_name=Lower('name'))
            if sortkey == 'blog_category':
                sortkey = 'blog_category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

        if 'blog_category' in request.GET:
            blog_categories = request.GET['category'].split(',')
            posts = posts.filter(blog_category__name__in=blog_categories)
            blog_categories = Blog_category.objects.filter(name__in=blog_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('posts'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = posts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'search_term': query,
        'current_categories': blog_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def post_view(request, post_id):
    """ A view to show individual posts """

    post = get_object_or_404(Post, pk=Post_id)

    context = {
        'post': post,
    }

    return render(request, 'posts/post_view.html', context)


@login_required
def add_post(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'posts/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_view ', args=[blog.id]))
        else:
            messages.error(request,
                           ('Failed to update post. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_post(request, blog_id):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Blog, pk=blog_id)
    product.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))