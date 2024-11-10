# relationship_app/urls.py
from django.urls import path
from .views import admin_view, librarian_view, member_view

app_name = 'relationship_app'

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]