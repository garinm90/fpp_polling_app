from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ShowViewSet

# urlpatterns = [
#     path('', ShowViewSet.as_view()),
# ]

router = DefaultRouter()

router.register(r'', ShowViewSet, basename='show')
urlpatterns = router.urls
