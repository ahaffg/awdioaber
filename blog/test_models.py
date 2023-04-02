from django.test import TestCase
from .models import Category, Blog


class TestBlogModels(TestCase):

    def test_string_representation(self):
        blog = Blog(name="Test Blog Name")
        self.assertEqual(str(blog), blog.name)

    def test_category_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")
