from django.urls import path
from users import views

app_name = 'users' # 1. Define our app's namespace.

urlpatterns = [ # 2. Create a urlpatterns array.
    path('new/', views.render_register_user_form, name='new'), # 3. Add our paths with its necessary parameters (url and view) and include the optional name parameter.
    path('register/', views.process_register_user_form, name='register'),
    path('login/', views.render_login_user_form, name='login'),
    path('authorize/', views.process_login_user_form, name='authorize'),
]