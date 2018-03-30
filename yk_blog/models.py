# coding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models
class Author(models.Model):#作者表
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    email = models.EmailField(verbose_name='作者邮箱')
    age = models.IntegerField(verbose_name='作者年龄',blank=True,null=True)
    gender = models.CharField(max_length=32,verbose_name='性别',blank=True)
    phone = models.CharField(max_length=32,verbose_name='手机',blank=True)
    address = models.CharField(max_length=32,verbose_name='地址',blank=True)
    photo = models.ImageField(upload_to='images',verbose_name='作者照片',blank=True)
    description = RichTextUploadingField(verbose_name='作者描述',blank=True)
    def __unicode__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='文章标题')
    time = models.DateField(max_length=32, verbose_name='发表日期')
    author = models.ForeignKey(Author)
    image = models.ImageField(upload_to='images',verbose_name='文章图片',blank=True)
    content= RichTextUploadingField(verbose_name='文章内容',blank=True)
    description = RichTextUploadingField(verbose_name='文章描述',blank=True)
