from django.urls import path
from . import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_view.member_dashboard, name='member_dashboard'),
]