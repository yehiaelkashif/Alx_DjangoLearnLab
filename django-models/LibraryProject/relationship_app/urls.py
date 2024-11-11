# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/add_book/', views.add_book, name='"add_book'),
    path('books/edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
