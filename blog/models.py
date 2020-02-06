from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    #摘要,blank为True时可为空
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    #多对一外键:放在多的一方
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    #多对多外键
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    #User外键:拉包引用
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)
    def get_absolute_url(self):#于是 reverse 函数会去解析这个视图函数对应的 URL，我们这里 detail 对应的规则就是 posts/<int:pk>/ int 部分会被后面传入的参数 pk 替换，所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，那么 get_absolute_url 函数返回的就是 /posts/255/ ，这样 Post 自己就生成了自己的 URL。
        return reverse('blog:detail', kwargs={'pk': self.pk})