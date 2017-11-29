from rest_framework import routers
from api.views import EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'^zoxon470', EmployeeViewSet, base_name='zoxon470')

urlpatterns = router.urls
