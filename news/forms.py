import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Category, News


class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    # is_published = forms.BooleanField(label='Опубликовать?', initial=True)
    # category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Category.objects.all(), label='Категория',
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match('\d', title):
            raise ValidationError('Название не должно начинаться c цифр')
        return title