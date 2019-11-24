from django.urls import path

from . import views
from .views import ArticlesListView, ArticlesDetailView, ArticlesCreateView, ArticlesUpdateView, ArticlesDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'web_app'
urlpatterns = [

    # path('recipe_list', views.recipe_list, name='recipe_list'),
    path('recipe_list', views.RecipeListView.as_view(), name='recipe_list'),
    path('articles_list', views.ArticlesListView.as_view(), name='articles_list'),
    path('articles_list/<str:username>', views.UserArticlesListView.as_view(), name='user_articles_list'),
    path('category_create', views.category_create, name="category_create"),
    path('articles_create', views.ArticlesCreateView.as_view(), name="articles_create"),
    path('<int:pk>/update', views.ArticlesUpdateView.as_view(), name='articles_update'),
    path('<int:pk>/delete', views.ArticlesDeleteView.as_view(), name='articles_delete'),
    path('<int:pk>/comment', views.add_comment_to_articles, name='articles_comment'),
    path('recipe_create', views.recipe_create, name="recipe_create"),
    path('<int:pk>', views.ArticlesDetailView.as_view(), name='articles_detail'),
    path('recipe_list/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),

]
