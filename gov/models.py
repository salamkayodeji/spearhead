from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from typing import Optional
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from slugify import slugify







# Create your models here.
class CategoryManager(models.Manager):
    def sort_file(self, slug):
        return self.filter(slug)

class Category(models.Model):
    category = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True, upload_to="headshots/")
    creator = models.ForeignKey(User, on_delete=models.CASCADE,)
    description = models.TextField(default='description', blank = True, null = True)
    coursename = models.CharField(max_length=50, blank = True, null = True)
    slug = models.SlugField(null=True, unique=True) # new
    popular = models.BooleanField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=254)
    objects = CategoryManager()



    
    class Meta:
        verbose_name_plural = "Categories"
    
    CategoryManager = models.Manager()

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('dash:category_detail', kwargs={'slug': self.slug})

    
class Post(models.Model):     
    coursecategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    content = RichTextField(default = 'content', blank = True, null = True)
    img = models.ImageField(null=True, blank=True, upload_to="headshots/")
    view_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    popular = models.BooleanField(null=True, blank=True)
    venue_1 = models.CharField(max_length=200, blank=True, null=True)
    venue_2 = models.CharField(max_length=200, blank=True, null=True)
    venue_3 = models.CharField(max_length=200, blank=True, null=True)
    venue_4 = models.CharField(max_length=200, blank=True, null=True)

    slug = models.SlugField(max_length=200, default='null')
    course_slug = models.SlugField(null=True) # new


    
    date_1 = models.DateField(null=True, blank=True)
    date_2 = models.DateField(null=True, blank=True)
    date_3 = models.DateField(null=True, blank=True)
    date_4 = models.DateField(null=True, blank=True) 
    date_5 = models.DateField(null=True, blank=True)
    date_6 = models.DateField(null=True, blank=True) 
    date_7 = models.DateField(null=True, blank=True)
    date_8 = models.DateField(null=True, blank=True)
    email = models.EmailField(default = 'Enter email here', max_length=254)
    banner = models.ImageField(null=True, blank=True, upload_to="headshots/")
    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.coursename

    def get_absolute_url(self):
        return reverse('gov:course_detail', kwargs={'slug': self.slug})
 

class event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    day = models.IntegerField()
    month= models.CharField(max_length=10)

class Gallery(models.Model):
    name = models.CharField(max_length=20)
    pic= models.ImageField(null=True, blank=True, upload_to="headshots/")

class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField( max_length=254)
    subject = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=False, blank= False ) 
   
