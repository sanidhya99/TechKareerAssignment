from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.demo.models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Authenticate the client

        # Create test data
        Post.objects.create(text="Test Post 1", user=self.user)
        Post.objects.create(text="Test Post 2", user=self.user)

    def test_post_list(self):
        # Make the API request
        response = self.client.get('/api/posts/')  # Ensure this matches your endpoint
        print(response)  # Debugging: Print response details
        self.assertEqual(response.status_code, 200)  # Check status code
