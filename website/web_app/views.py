from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Recipe, Category, Comments
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts import views as acc
from . import forms
from django.contrib import messages
# Create your views here.
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse


#
# def articles_list(request):
#     articles = Articles.objects.all().order_by('-date')
#     return render(request, "articles_list.html", {'articles_list': articles})

class ArticlesListView(ListView):
    model = Articles
    template_name = "articles_list.html"
    context_object_name = "articles_list"
    ordering = ['-date']
    paginate_by = 4


class UserArticlesListView(ListView):
    model = Articles
    template_name = "user_articles_list.html"
    context_object_name = "user_articles_list"
    ordering = ['-date']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Articles.objects.filter(author=user).order_by('-date')


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = "articles_detail.html"
    context_object_name = "articles_detail"


class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    fields = ['title', 'body', 'thumb', 'category', 'recipe']
    template_name = "articles_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ['title', 'body', 'slug', 'thumb', 'category', 'recipe']
    template_name = "articles_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = "articles_confirm_delete.html"
    context_object_name = "articles_delete"

    success_url = reverse_lazy('web_app:articles_list')

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


@login_required
def add_comment_to_articles(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('web_app:articles_detail', pk=article.pk)
    else:
        form = forms.CreateComment()
    return render(request, 'articles_comment.html', {'form': form})


@login_required(login_url="/accounts/login/")
def articles_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('web_app:articles_list')
    else:

        form = forms.CreateArticle()
    return render(request, "articles_create.html", {'form': form})


@login_required(login_url="/accounts/login/")
def category_create(request):
    if request.method == "POST":
        form = forms.CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('web_app:articles_list')
    else:

        form = forms.CreateCategory()
    return render(request, "category_create.html", {'form': form})


@login_required(login_url="/accounts/login/")
def recipe_create(request):
    if request.method == "POST":
        form = forms.CreateRecipe(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('web_app:articles_list')
    else:

        form = forms.CreateRecipe()
    return render(request, "recipe_create.html", {'form': form})


def recipe_list(request):
    recipes = Recipe.objects.all().order_by('title')
    return render(request, "recipe_list.html", {'recipes': recipes})

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"
    context_object_name = "recipe_list"
    ordering = ['title']
    paginate_by = 4

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe_detail"