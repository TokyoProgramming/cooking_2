from django import forms
from .models import featuredPost, Post


class f_postForm(forms.ModelForm):
    class Meta:
        model = featuredPost
        fields = [
            'featured_field',
            'featured_tittle',
            'featured_text',
            'featured_image',
        ]



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'blog_field',
            'blog_tittle',
            'blog_text',
            'blog_image',

        ]
