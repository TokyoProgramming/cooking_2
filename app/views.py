from django.shortcuts import render
from blog.models import Post

def about(request):
    return render(request, 'pages/about.html')


def search(request):
    queryset_list = Post.objects.order_by('-published_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            queryset_list = queryset_list.filter(blog_field__icontains=keywords)


    context = {
        'posts': queryset_list,

    }

    return render(request, 'pages/search.html', context)



