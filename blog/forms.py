from django import forms
from .models import Post

class  BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('blog_field', 'blog_tittle', 'blog_text', 'blog_image', )
