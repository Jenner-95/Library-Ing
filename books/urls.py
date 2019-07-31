from django.urls import path
from books import views


app_name = 'books'

urlpatterns = [
    path('catalogue/<int:user_id>/', views.render_book_catalogue, name='catalogue'),
    path('new/<int:user_id>/', views.render_create_book_form, name='new'),
    path('add/', views.process_create_book_form, name='add'),
    path('edit/<int:book_id>/', views.render_edit_book_form, name='edit'),
    path('save/<int:book_id>/', views.process_edit_book_form, name='save'),
    path('delete/<int:book_id>/', views.delete_book, name='delete'),
]