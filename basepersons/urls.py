
from django.urls import path, re_path
from . import views



urlpatterns = [



    path('login_user', views.loginUser, name='login-user'),
    path('homepage', views.sitehomepage, name='site-home'),
    path('create_acc', views.createAccount, name='create-account'),

    path('login', views.loginPage, name='login'),

    path('create_account', views.createAccount, name='createaccount'),

   

]


