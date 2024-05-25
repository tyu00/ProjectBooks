from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = []

urlpatterns += router.urls
