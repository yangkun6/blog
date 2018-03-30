# coding:utf-8
from django.shortcuts import render
from models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Author

# Create your views here.
class Paging(Paginator):
    def __init__(self,current_page,per_page_num,*args,**kwargs):
        Paginator.__init__(self,*args,**kwargs)
        self.current_page=int(current_page)
        self.per_page_num=int(per_page_num)
    def pager_num_range(self):
        if self.num_pages<self.per_page_num:
            return range(1, self.num_pages+1)
        part = int(self.per_page_num//2)
        if self.current_page <= part:
            return range(1, self.per_page_num+1)
        elif (self.current_page+part) > self.num_pages:
            return range(self.num_pages-self.per_page_num, self.num_pages+1)
        else:
            return range(self.current_page-part, self.current_page+part+1)
def index (request):
    article_list = Article.objects.all()
    return render(request, 'index.html', locals())
def about(request):
    return render(request, 'about.html', locals())
def photo(request):
    return render(request, 'photo.html', locals())
def article(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    user_list = article.content
    current_page = request.GET.get("p")

    paginator = Paging(current_page, 7, user_list,479)

    try:
        data = paginator.page(current_page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'article.html', locals())
def message(request):
    return render(request, 'message.html', locals())