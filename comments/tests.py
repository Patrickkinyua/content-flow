from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from content.models import article
from .models import Comment


class CommentLikeTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='commenter', password='password')
        self.client.force_authenticate(user=self.user)
        self.article = article.objects.create(title='foo', body='bar', author=self.user)
        self.comment = Comment.objects.create(article=self.article, author=self.user, content='hi')

    def test_like_and_unlike(self):
        base = reverse('comment-detail', kwargs={'article_pk': self.article.pk, 'pk': self.comment.pk})
        resp = self.client.get(base)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('like_count'), 0)
        self.assertFalse(resp.data.get('liked'))

        resp = self.client.post(base + 'like/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['status'], 'liked')

        resp = self.client.get(base)
        self.assertEqual(resp.data.get('like_count'), 1)
        self.assertTrue(resp.data.get('liked'))

        resp = self.client.post(base + 'like/')
        self.assertEqual(resp.data['status'], 'already liked')

        resp = self.client.post(base + 'unlike/')
        self.assertEqual(resp.data['status'], 'unliked')

        resp = self.client.get(base)
        self.assertEqual(resp.data.get('like_count'), 0)
        self.assertFalse(resp.data.get('liked'))
