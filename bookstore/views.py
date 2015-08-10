from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookstore.models import Books
from bookstore.serializer import BooksSerializer

# Create your views here.

def book_list(request):
    return render(request, 'bookstore/book_list.html', {})

@api_view(['GET', 'POST'])
def book_list(request, format=None):
	if request.method == 'GET':
		books = Books.objects.all()
		serializer = BooksSerializer(books, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = BooksSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk, format=None):
	try:
		book = Books.objects.get(pk=pk)
	except Books.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BooksSerializer(book)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = BooksSerializer(books, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
