from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('new/', views.render_register_user_form, name='new'),
    path('register/', views.process_register_user_form, name='register'),
    path('login/', views.render_login_user_form, name='login'),
    path('authorize/', views.process_login_user_form, name='authorize'),
]