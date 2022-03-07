from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

class ArticleViewSet(ViewSet):
    model = Article
    queryset = Article.objects.all()

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
