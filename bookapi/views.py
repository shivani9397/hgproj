from django.shortcuts import render

# Create your views here.
from .models import Book
from .serilizers import BookSerialization
from rest_framework.viewsets import ModelViewSet

#GET GET/{id} POST PUT PATCH DELETE
class BookOperations(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialization
