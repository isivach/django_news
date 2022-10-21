from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Новость')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_created= True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})


    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
