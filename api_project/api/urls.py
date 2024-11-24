from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from django.urls import path, include

# Initialize the router
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (if still needed for listing)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router-generated URLs
    path('', include(router.urls)),
]
