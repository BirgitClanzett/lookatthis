from django.contrib import admin
from .models import Articles, Category, Recipe, Comments

# Register your models here.

admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comments)
