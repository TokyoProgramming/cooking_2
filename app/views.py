from django.shortcuts import render

def hello(request):
    return render(request, 'sample/hello.html')

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def search(request):
    return render(request, 'pages/search.html')

def contact(request):
    return render(request, 'pages/contact.html')

def homepage_2(request):
    return render(request, 'pages/homepage-2.html')

def category(request):
    return render(request, 'pages/category.html')
