from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import featuredPost, Post
# from .forms import f_postForm, PostForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.core.paginator import Paginator



def index(request):
    posts = Post.objects.order_by('-published_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    context = {
        'featured_posts': featuredPost.objects.all(),
        'posts': paged_post,

    }
    return render(request, 'pages/index.html', context)


def createBlog(request):
    if request.method == 'POST':
        blog_field = request.POST['blog_field']
        blog_tittle = request.POST['blog_tittle']
        blog_text = request.POST['blog_text']
        blog_image = request.FILES['blog_image']

        blog = Post.objects.create(
            blog_field=blog_field,
            blog_tittle=blog_tittle,
            blog_text=blog_text,
            blog_image=blog_image,
        )
        blog.save()

        return redirect('index')

    return render(request, 'pages/create-blog.html')


def blogDetail(request, post_id):
    single_blog = get_object_or_404(Post, id=post_id)
    limiting_blog = Post.objects.order_by('-published_date')[:3]

    context = {
        'single_blog': single_blog,
        'limiting_blog': limiting_blog,
    }

    return render(request, 'pages/blog-single.html', context)
