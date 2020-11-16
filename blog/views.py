from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import featuredPost, Post
from .forms import f_postForm, PostForm



def index(request):
    context = {
        'featured_posts': featuredPost.objects.all(),
        'posts': Post.objects.all(),

    }

    return render(request, 'pages/index.html', context)



class TestFormView(CreateView):
    template_name = 'test/create_test.html'
    form_class = f_postForm
    success_url = reverse_lazy('success_view')



class SuccessView(TemplateView):
    template_name = "test/success.html"

