from django.shortcuts import render, redirect
from django.contrib import messages
from .models import featuredPost, Post


def index(request):
    context = {
        'featured_posts': featuredPost.objects.all(),
        'posts': Post.objects.all(),

    }

    return render(request, 'pages/index.html', context)



# def index(request):
# if request.method == 'POST':
#     featured_field = request.POST['featured_field']
#     featured_title = request.POST['featured_title']
#     featured_text = request.POST['featured_text']
#     featured_image = request.POST['featured_image']
#
#     featured_post = featuredPost.objects.create(
#         featured_field=featured_field,
#         featured_title=featured_title,
#         featured_text=featured_text,
#         featured_image=featured_image
#     )
#
#     featured_post.save()
#     return render(request, 'pages/index.html')
#
#
# elif request.method== 'GET':
#
#
#     return render(request, 'pages/index.html')

# return render(request, 'pages/index.html')


