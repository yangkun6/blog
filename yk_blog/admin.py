# coding:utf-8
from django.contrib import admin
from models import *
# Register your models here.
class AriticleAdmin(admin.ModelAdmin):#admin后台文章优化
    list_display = ('title','author','time')#列表字段展示
    search_fields = ('title','author')#搜索指定内容
    list_filter = ('time',)#过滤器的内容
class AuthorAdmin(admin.ModelAdmin):#admin后台作者优化
    list_display = ('name','age','gender')#列表字段有的内容
admin.site.register(Article,AriticleAdmin)
admin.site.register(Author,AuthorAdmin)