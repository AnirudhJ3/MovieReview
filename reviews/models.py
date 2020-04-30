from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    movie_name = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    review = models.TextField(max_length=500)
    star = models.IntegerField()
