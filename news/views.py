from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from news.forms import NewsForm
from news.models import Category, News


class HomeNews(ListView):
    model = News

class IndexView(TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = {
            'news' : News.objects.all(),
            'title' : 'Список новостей',
                   }
        return context

class CreatCategoryView(CreateView):
    template_name = "news/create_author.html"
    model = Category
    fields = '__all__'
    success_url = '/'

class UpdateCategoryView(UpdateView):
    template_name = "news/create_author.html"
    model = Category
    fields = '__all__'
    success_url = '/'

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.filter(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'title': category.first()})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})