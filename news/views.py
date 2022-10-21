from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from news.models import Category, News

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {
            'news' : News.objects.all(),
            'title' : 'Список новостей',
                   }
        return context

class CreatCategoryView(CreateView):
    template_name = "create_author.html"
    model = Category
    fields = '__all__'
    success_url = '/'

class UpdateCategoryView(UpdateView):
    template_name = "create_author.html"
    model = Category
    fields = '__all__'
    success_url = '/'

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.filter(pk=category_id)
    return render(request, 'category.html', {'news': news, 'title': category.first()})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'view_news.html', {'news_item': news_item})
