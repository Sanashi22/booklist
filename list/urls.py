from django.urls import path
from .views import book_list, add_book, edit_book
app_name= "book"
urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
]
