from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from book import BookSerializer
from book.models import BookInfo


class BookView(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer.BookViewSetSerializer

