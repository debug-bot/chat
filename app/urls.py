from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('' , Home , name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
    path('forget-password/' , ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('logout/' , Logout , name="logout"),
    # path('process/' , process , name="process"),
    path('about/', about, name="about"),
    path('toxssin_chat/', handle_textarea, name='handle_textarea'),
    path('new_home/', new_home, name='new_home'),
    
    
 
]
