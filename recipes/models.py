from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeUnit(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class ServingsUnit(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.ForeignKey(TimeUnit, on_delete=models.SET_NULL, null=True)
    servings = models.IntegerField()
    servings_unit = models.ForeignKey(ServingsUnit, on_delete=models.SET_NULL, null=True)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title
