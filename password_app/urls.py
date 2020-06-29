from django.urls import path, include
from password_app import views

# TEMPLATE URLs
app_name = 'password_app'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
