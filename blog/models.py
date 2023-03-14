from django.db import models
from django.db.models.signals import pre_save
from profiles.models import User
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=150)
    content = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog:delete', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('blog:like', kwargs={'slug': self.slug})

    @property
    def get_comment_count(self):
        return self.blogcomment_set.all().count()

    @property
    def get_view_count(self):
        return self.blogview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def blogcomments(self):
        return self.blogcomment_set.all()


def create_slug(instance, new_slug=None):
    """Slugifys the title, if slug exists it adds a id to make it unique
    (Logic by CodingEntrepreneurs)."""
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def post_save_blog_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(post_save_blog_receiver, sender=Blog)


class BlogComment(models.Model):
    """To be able to comment on a blog."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class BlogView(models.Model):
    """Keeps track of views."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):

    """To keep track of all the likes."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username