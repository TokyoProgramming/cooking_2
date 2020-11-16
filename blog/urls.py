from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:post_id>/', views.blogDetail, name='blog-single'),
    path('test/create_test/', views.TestFormView.as_view(), name='create_test'),
    path('test/success/', views.SuccessView.as_view(), name='success_view'),
]
