from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import featuredPost, Post
from .forms import f_postForm, PostForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.core.paginator import Paginator


def index(request):

    posts = Post.objects.all()
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    context = {
        'featured_posts': featuredPost.objects.all(),
        'posts': paged_post,

    }
    return render(request, 'pages/index.html', context)


def blogDetail(request, post_id):

    single_blog = Post.objects.get(id=post_id)
    limiting_blog = Post.objects.all()[:3]

    context = {
        'single_blog' : single_blog,
        'limiting_blog' : limiting_blog,
    }

    return render(request, 'pages/blog-single.html', context)





class TestFormView(BSModalCreateView):
    template_name = 'test/create_test.html'
    form_class = f_postForm
    success_url = reverse_lazy('success_view')



class SuccessView(TemplateView):
    template_name = "test/success.html"

