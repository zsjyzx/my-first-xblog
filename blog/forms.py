#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import re
import markdown

from django import forms

from models import Article
#from models import ExampleModel

from mdeditor.fields import MDTextFormField
#from mdeditor.fields import MDTextField

class ArticlePublishForm(forms.Form):
    title = forms.CharField(
        label=u'文章标题',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'vTextField', 'placeholder': u'文章标题，请在标题末尾添加".html"'}),
    )

    content = MDTextFormField(
        label=u'文章内容',
        min_length=10,
        widget=forms.Textarea(),
    )

    tags = forms.CharField(
        label=u'文章标签',
        max_length=30,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'文章标签，以空格进行分割'}),
    )

    def save(self, username, article=None):
        cd = self.cleaned_data
        title = cd['title']
        title_zh = title
        now = datetime.datetime.now()
        content_md = cd['content']
        #content_html = markdown.markdown(cd['content'])
        content_html = markdown.markdown(cd['content'], extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])
        re_title = '<h\d>(.+)</h\d>'
        data = content_html.split('\n')
        for line in data:
            title_info = re.findall(re_title, line)
            if title_info:
                title_zh = title_info[0]
                break
        url = '/article/%s' % (title)
        tags = cd['tags']
        if article:
            article.url = url
            article.title = title
            article.title_zh = title_zh
            article.content_md = content_md
            article.content_html = content_html
            article.tags = tags
            article.updated = now
        else:
            article = Article(
                url=url,
                title=title,
                title_zh=title_zh,
                author=username,
                content_md=content_md,
                content_html=content_html,
                tags=tags,
                views=0,
                created=now,
                updated=now)
        article.save()

#class MDEditorForm(forms.Form):
#    name = forms.CharField()
#    content = MDTextFormField()

# ModelForm 可自动将model 对应的字段转为 form字段
#class MDEditorModleForm(forms.ModelForm):
#    class Meta:
#        model = ExampleModel
#        fields = '__all__'

class ArticleModleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
