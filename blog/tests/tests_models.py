from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Category, Blog, BlogComment, BlogView, Like
from memberships.models import *


class TestCreateBlogModels(TestCase):
    """testing the creation on a blog """

    fixtures = [
        'memberships.json',
        'user.json'
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def setUp(self):
        self.user = User.objects.get(username="tester")

    def test_create_Blog(self):
        newblog = Blog.objects.create(
            title='newblog',
            author=self.user,
            category="testingCatergory",
            content='testing loads of stuff',
            slug='testing',
        )
        self.assertTrue(isinstance(newblog, Blog))


class TestBlog(TestCase):
    """Testing the blog details and get_absolute_url() """

    fixtures = [
        'memberships.json',
        'user.json'
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def setUp(self):
        self.user = User.objects.get(username="tester")

        newblog = Blog.objects.create(
            title='newblog',
            author=self.user,
            category="testingCatergory",
            content='testing loads of stuff',
            slug='testing',
        )

    def test_get_absolute_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_update_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_delete_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_like_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_blog_title(self):
        newblog = Blog.objects.get(id=1)
        self.assertTrue(newblog.title, 'newblog')

    def test_get_blog_author(self):
        newblog = Blog.objects.get(id=1)
        self.assertTrue(newblog.author, 'tester')

    def test_get_blog_category(self):
        newblog = Blog.objects.get(id=1)
        self.assertTrue(newblog.category, 'testingCatergory')

    def test_blog_string(self):
        newblog = Blog.objects.get(id=1)
        self.assertEqual(newblog.__str__(), newblog.title)


class TestCategory(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='TestCat')

    def setUp(self):
        self.name = Category.objects.get(name='TestCat')

    def test_create_category(self):
        catergory = Category.objects.create(name=self.name)
        self.assertTrue(isinstance(catergory, Category))

    def test_category_string(self):
        catergory = Category.objects.create(name=self.name)
        self.assertEqual(catergory.__str__(), self.name)
        