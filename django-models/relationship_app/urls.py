# relationship_app/urls.py
from django.urls import path
from .views import login_view, logout_view, register_view  # import register_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'relationship_app'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),  # Add the custom register view here
]
