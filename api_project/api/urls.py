from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Previous list view
    path('', include(router.urls)),  # Include router URLs for CRUD operations
]
