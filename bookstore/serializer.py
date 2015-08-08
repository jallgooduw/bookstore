from django.forms import widgets
from rest_framework import serializers
from bookstore.models import Books

class BooksSerializer(serializers.ModelSerializer):
        class Meta:
                model = Books
                fields = ('id', 'title', 'author', 'pubdate', 'publisher', 'summary', 'price', 'buylink', 'coverimg')

def create(self, validated_data):
	return Books.objects.create(**validated_data)

def update(self, instance, validated_data):
	instance.title = validate_data.get('title', instance.title)
	instance.author = validate_data.get('author', instance.author)
	instance.pubdate = validate_data.get('pubdate', instance.pubdate)
	instance.publisher = validate_data.get('publisher', instance.publisher)
	instance.summary = validate_data.get('summary', instance.summary)
	instance.price = validate_data.get('price', instance.price)
	instance.buylink = validate_data.get('buylink', instance.buylink)
	instance.coverimg = validate_data.get('coverimg', instance.coverimg)
	instance.save()
	return instance
