from rest_framework import routers
from api.views import TrackingUserViewSet


router = routers.DefaultRouter()
router.register(r'user', TrackingUserViewSet, base_name='user')

urlpatterns = router.urls