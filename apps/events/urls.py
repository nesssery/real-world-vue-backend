from rest_framework import routers
from apps.events.views import EventViewSet, CategorieViewSet

router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')
router.register('api/categories', CategorieViewSet, 'categories')

urlpatterns = router.urls
