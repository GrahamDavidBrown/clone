from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=25)


class User_Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.ForeignKey(City)


class Category(models.Model):
    category = models.CharField(max_length=20)


class Sub_Category(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category)


class Listing(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    picture_link = models.URLField(max_length=1000, null=True, blank=True)
    owner = models.ForeignKey(User_Profile)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Sub_Category)
    city = models.ForeignKey(City)
