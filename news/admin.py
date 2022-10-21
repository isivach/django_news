from django.contrib import admin
from news.models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title', 'created_at', 'updated_at', 'photo', 'is_published')
    list_display_links = ('title', )
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')

admin.site.register(Category)
# admin.site.register(Genre)
admin.site.register(News, NewsAdmin)