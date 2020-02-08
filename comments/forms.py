from django import forms
from .models import Comment

#最下层为model,然后在上面创建了CommentForm类,相当于封装了一个表单出来
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']