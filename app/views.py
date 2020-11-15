from django.shortcuts import render






def about(request):
    return render(request, 'pages/about.html')


def search(request):
    return render(request, 'pages/search.html')




#
# def homepage_2(request):
#     return render(request, 'pages/homepage-2.html')
#
#
# def category(request):
#     return render(request, 'pages/category.html')
