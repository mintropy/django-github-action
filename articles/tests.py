from django.test import TestCase

from model_bakery import baker

from .models import Article


class TestArticle(TestCase):
    """model test class
    article
    """
    def test_creation_article(self):
        article = baker.make(Article)
        self.assertEqual(str(article), article.title)
