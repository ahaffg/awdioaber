from django.db import models

class Category(models.Model):

class Meta:
        verbose_name_plural = 'Blog_categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Blog(models.Model):
    blog_category = models.ForeignKey('Blog_category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    blog_text = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name