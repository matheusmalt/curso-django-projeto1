from django.contrib import admin
from .models import Category, Recipe, TimeUnit, ServingsUnit
# Register your models here.


@admin.register(TimeUnit)
class TimeUnitAdmin(admin.ModelAdmin):
    ...

@admin.register(ServingsUnit)
class ServingsunitAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...