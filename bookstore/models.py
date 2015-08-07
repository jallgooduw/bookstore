from django.db import models
from django.utils import timezone


# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	pubdate = models.DateTimeField()
	publisher = models.CharField(max_length=200)
	summary = models.TextField()
	price = models.FloatField()
	buylink = models.URLField()
	coverimg = models.URLField()

