from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from model_bakery import baker

from .models import Article


class TestArticle(TestCase):
    """model test class
    article
    """
    def test_creation_article(self):
        article = baker.make(Article)
        self.assertEqual(str(article), article.title)


class TestArticleAPI(APITestCase):
    def test_article_list(self):
        url = reverse('article_list')
