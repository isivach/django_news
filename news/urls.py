from django.urls import path, include
from news.views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('test/',CreatCategoryView.as_view()),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
]