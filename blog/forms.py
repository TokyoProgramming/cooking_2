from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import featuredPost, Post


class f_postForm(BSModalModelForm):
    class Meta:
        model = featuredPost
        fields = [
            'featured_field',
            'featured_tittle',
            'featured_text',
            'featured_image',
        ]



class PostForm(BSModalModelForm):
    class Meta:
        model = Post
        fields = [
            'blog_field',
            'blog_tittle',
            'blog_text',
            'blog_image',

        ]
