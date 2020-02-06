from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'author']#显示每行需要显示的内容
    fields = ['title', 'body', 'excerpt', 'category', 'tag']#显示可修改的列
    def save_model(self, request, obj, form, change):#关联request.user,Post实例的时候将该实例认证user
        obj.author = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
