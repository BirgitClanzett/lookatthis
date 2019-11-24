from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse, reverse_lazy


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(default="default.png", blank=True)
    ingredients = models.TextField()
    preparation = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug

    def snippet(self):
        return self.body[:200] + '  ...'

    def get_absolute_url(self):
        return reverse("web_app:articles_detail", kwargs={'pk': self.pk})


class Comments(models.Model):
    article = models.ForeignKey(Articles, related_name="comments",default=None, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("web_app:articles_detail", kwargs={'pk': self.pk})

    def comment_approved(self):
            self.approved_comment = True
            self.save()

