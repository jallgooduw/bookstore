from django.forms import widgets
from rest_framework import serializers
from bookstore.models import Books


class BooksSerializer(serializers.ModelSerializer):
	title = serializers.CharField(max_length=200)
        author = serializers.CharField(max_length=200)
        pubdate = serializers.DateTimeField()
        publisher = serializers.CharField(max_length=200)
        summary = serializers.TextField()
        price = serializers.FloatField()
        buylink = serializers.URLField()
        coverimg = serializers.URLField()

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

class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Books
		fields = ('title', 'author', 'pubdate', 'publisher', 'summary', 'buylink', 'coverimg')
