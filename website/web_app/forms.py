from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['title', 'body', 'thumb', 'category',]


class CreateCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['title', 'image', ]


class CreateRecipe(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'subtitle', 'image', 'ingredients', 'preparation']


class UpdateArticle(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['title', 'body', 'slug', 'category', 'recipe']


class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['author', 'body', ]
