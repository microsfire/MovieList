from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = router.urls