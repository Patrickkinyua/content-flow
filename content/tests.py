from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import article


class ArticleLikeTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='tester', password='password')
        self.client.force_authenticate(user=self.user)
        self.article = article.objects.create(title='foo', body='bar', author=self.user)

    def test_like_and_unlike(self):
        url = reverse('content-detail', args=[self.article.pk])
        # initially no likes
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('like_count'), 0)
        self.assertFalse(resp.data.get('liked'))

        # like the article
        like_url = url + 'like/'
        resp = self.client.post(like_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['status'], 'liked')

        # retrieving again shows liked
        resp = self.client.get(url)
        self.assertEqual(resp.data.get('like_count'), 1)
        self.assertTrue(resp.data.get('liked'))

        # liking again returns already liked
        resp = self.client.post(like_url)
        self.assertEqual(resp.data['status'], 'already liked')

        # unlike
        unlike_url = url + 'unlike/'
        resp = self.client.post(unlike_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['status'], 'unliked')

        resp = self.client.get(url)
        self.assertEqual(resp.data.get('like_count'), 0)
        self.assertFalse(resp.data.get('liked'))
