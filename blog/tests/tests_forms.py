from django.test import TestCase
from blog.forms import BlogForm, BlogCommentForm
from blog.models import *


class TestBlogForm(TestCase):

    def test_order_form_required(self):
        invalid_data = {
            'title': '',
            'category': '',
            'content': '',
            'thumbnail': '',
        }
        form = BlogForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('title', form.errors.keys())
        self.assertIn('category', form.errors.keys())
        self.assertIn('thumbnail', form.errors.keys())

    def test_blog_form_metaclass(self):
        form = BlogForm()
        self.assertEqual(form.Meta.fields,
                         ('title', 'category', 'content', 'thumbnail',))


class TestBlogCommentForm(TestCase):

    def test_order_blog_comment_form_required(self):
        form = BlogCommentForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('content', form.errors.keys())

    def test_blog_comment_form_metaclass(self):
        form = BlogCommentForm()
        self.assertEqual(form.Meta.fields, ('content',))
