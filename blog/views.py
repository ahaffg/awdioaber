from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogView, Like,  Category
from .forms import BlogCommentForm, BlogForm


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    ordering = ['-publish_date']
    context_object_name = 'all_blogs'

    def get_context_data(self, **kwargs):
        feature_blog = Blog.objects.filter(featured=True)
        category_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['feature_blog'] = feature_blog
        context['category_menu'] = category_menu
        return context


class SearchView(View):
    template_name = 'blog/blog_search.html'

    def get(self, request, *args, **kwargs):
        all_blogs = Blog.objects.all()
        category_menu = Category.objects.all()
        query = None

        if 's' in request.GET:
            query = request.GET['s']
            if not query:
                messages.error(request, "Sorry! No Input? Try again Please")
                return redirect(reverse('blog:list'))
            search = Q(title__icontains=query) | Q(content__icontains=query)
            all_blogs = all_blogs.filter(search)

        context = {
            'search_words': query,
            'all_blogs': all_blogs,
            'category_menu': category_menu,
        }
        return render(request, 'blog/blog_search.html', context)


def CategoryView(request, category):
    category_blogs = Blog.objects.filter(category=category)
    category_menu = Category.objects.all()
    all_blogs = Blog.objects.all()
    context = {
        'category': category,
        'category_blogs': category_blogs,
        'category_menu': category_menu,
        'all_blogs': all_blogs
    }
    return render(request, 'blog/blog_categories.html', context)


class BlogDetailView(DetailView):
    """(Logic by Mat @ JustDjango) Understood and implemented."""

    model = Blog

    def post(self, *args, **kwargs):
        """Adding comments to blogs."""
        form = BlogCommentForm(self.request.POST)
        if form.is_valid():
            blog = self.get_object()
            blogcomment = form.instance
            blogcomment.user = self.request.user
            blogcomment.blog = blog
            blogcomment.save()
            return redirect("blog:details", slug=blog.slug)
        return redirect("blog:details", slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': BlogCommentForm()

        })
        return context

    def get_object(self, **kwargs):
        """Counts the number of authenticated users view the blog."""
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            BlogView.objects.get_or_create(user=self.request.user, blog=object)
        return object


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Uses the 'blog_form.html' as it needs the inputs,
    The context is changed to 'create', 
    (Logic by Mat @ JustDjango) Understood and implemented.
    """
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Uses the 'blog_form.html' as it needs the inputs,
    The context is changed to 'Update', 
    (Logic by Mat @ JustDjango) Understood and implemented.
    """
    form_class = BlogForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = '/blog/'


class BlogAuthorPageView(LoginRequiredMixin, View):
    template_name = 'blog/blog_authors.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(User, id=self.kwargs['pk'])
        user_blog = Blog.objects.filter(
            author=user_profile.id).order_by('-publish_date')
        context = {
            'page_user': user_profile,
            'user_blog': user_blog,
        }
        return render(request, 'blog/blog_authors.html', context)


@ login_required()
def like(request, slug):
    """Checks to see if the use has liked the blog
    If True, then delete the like if False then create the like
    (Logic by Mat @ JustDjango) Understood and implemented."""

    blog = get_object_or_404(Blog, slug=slug)
    like_qs = Like.objects.filter(user=request.user, blog=blog)

    if like_qs.exists():
        # unlike the post
        like_qs[0].delete()
        return redirect('blog:details', slug=slug)

    Like.objects.create(user=request.user, blog=blog)
    return redirect('blog:details', slug=slug)
