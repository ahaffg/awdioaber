from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse
from blog.views import *
from blog.models import *


class TestBlogListViews(TestCase):
    fixtures = [
        'memberships.json',
        'user.json',
        'test_blog.json',
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_blog_list_view(self):
        resp = self.client.get(reverse('blog:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_list.html')
        self.assertTrue('feature_blog' in resp.context)
        self.assertTrue('category_menu' in resp.context)
        self.assertTrue('all_blogs' in resp.context)
        self.assertTrue('feature_blog' in resp.context)
        self.assertTrue('category_menu' in resp.context)


# Testing Blog Search View

    def test_blog_search_post(self):
        resp = self.client.get(
            '/blog/search/?', {'s': 'Immune+system'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['search_words'], 'Immune+system')
        self.assertTemplateUsed(resp, template_name='blog/blog_search.html')

    def test_blog_search_Error_message_post(self):
        resp = self.client.get(
            '/blog/search/?', {'s': ''})
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Sorry! No Input? Try again Please")


# Testing Blog Create and Update Views

    def test_abstract_user_blog_create_view(self):
        resp = self.client.get(reverse('blog:create'))
        self.assertRedirects(resp, '/accounts/login/?next=/blog/create/')
        self.assertEqual(resp.status_code, 302)

    def test_logged_in_user_blog_create_view(self):
        resp = self.client.get(reverse('blog:create'))
        self.assertEqual(resp.status_code, 302)

    def test_create_blog_context_in_view(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get('/blog/create/')
        self.assertEqual(resp.context['view_type'], 'create')
        self.assertTemplateUsed(resp, template_name='blog/blog_form.html')
        self.assertEqual(resp.status_code, 200)

    def test_Update_blog_context_in_view(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        slug = Blog.objects.get(id=1)
        blog_slug = slug.slug
        resp = self.client.get(f'/blog/{blog_slug}/update/')
        self.assertEqual(resp.context['view_type'], 'update')
        self.assertTemplateUsed(resp, template_name='blog/blog_form.html')
        self.assertEqual(resp.status_code, 200)

# Testing Blog Category View
    def test_blog_category_view(self):
        cat = Category.objects.get(id=2)
        cat_name = cat.name
        resp = self.client.post(f'/blog/category/{cat_name}/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name='blog/blog_categories.html')
        self.assertTrue('category' in resp.context)
        self.assertTrue('category_blogs' in resp.context)
        self.assertTrue('category_menu' in resp.context)
        self.assertTrue('all_blogs' in resp.context)

# Testing Blog Detail View
    def test_blog_detail_view(self):
        blog = Blog.objects.get(id=2)
        blog_slug = blog.slug
        resp = self.client.get(f'/blog/{blog_slug}/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_detail.html')

    def test_blog_comment_view_vaild_post(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        blog = Blog.objects.get(id=2)
        blog_slug = blog.slug
        resp = self.client.post(
            f'/blog/{blog_slug}/', {'rating': '5', 'content': 'Nice Blog'})
        self.assertRedirects(resp, "/blog/how-to-support-your-immune-system/")
        self.assertEqual(resp.status_code, 302)
