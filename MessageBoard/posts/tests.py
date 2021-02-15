from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Test text")
    
    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f"{post.text}"
        self.assertEqual(expected_object_name, "Test text")

class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text='This is another test')
    
    def test_url_exist_at_correct_loc(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')