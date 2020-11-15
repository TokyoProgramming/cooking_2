from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
    path('password_change_reset/', views.password_change_reset, name='password_change_reset'),
    path('password_change_reset/done', views.password_change_reset_done, name='password_change_reset_done'),
    path('reset/', views.password_reset_conrifm, name='password_reset_conrifm'),
    path('reset/done/', views.reset_done, name='reset_done'),

]


# account/ login/ [name='login']
# account/ logout/ [name='logout']
# account/ password_change/ [name='password_change']
# account/ password_change/done/ [name='password_change_done']
# account/ password_reset/ [name='password_reset']
# account/ password_reset/done/ [name='password_reset_done']
# account/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# account/ reset/done/ [name='password_reset_complete']

