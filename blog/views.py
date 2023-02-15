from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Article, Blog_category
from .forms import ArticleForm

# Create your views here.


def all_articles(request):
    """ A view to show all posts, including sorting and search queries """

    articles = Article.objects.all()
    query = None
    blog_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                posts = articles.annotate(lower_name=Lower('title'))
            if sortkey == 'blog_category':
                sortkey = 'blog_category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

        if 'blog_category' in request.GET:
            blog_categories = request.GET['blog_category'].split(',')
            posts = posts.filter(blog_category__name__in=blog_categories)
            blog_categories = Blog_category.objects.filter(name__in=blog_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('articles'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            posts = articles.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'articles': articles,
        'search_term': query,
        'current_blog_categories': blog_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'posts/blog.html', context)


def article_view(request, article_id):
    """ A view to show an individual post """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'articles': articles,
    }

    return render(request, 'articles/article_view.html', context)


@login_required
def add_article(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('article_view', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to add post. '
                            'Please ensure the form is valid.'))
    else:
        form = ArticleForm()

    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, blog_id):
    """ Edit a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_view ', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to update post. '
                            'Please ensure the form is valid.'))
        else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.name}')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Blog, pk=article_id)
    article.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))