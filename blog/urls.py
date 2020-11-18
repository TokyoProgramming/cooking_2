from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('create-blog/', views.createBlog, name='create-blog'),
    path('<int:post_id>/', views.blogDetail, name='blog-detail'),
    path('<int:post_id>/update/', views.blogUpdate, name='update-blog'),

]
