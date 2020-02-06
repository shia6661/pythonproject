from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #摘要,blank为True时可为空
    excerpt = models.CharField(max_length=200, blank=True)
    #多对一外键:放在多的一方
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #多对多外键
    tag = models.ManyToManyField(Tag, blank=True)
    #User外键:拉包引用
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title