from rest_framework import routers
from api.views import EmployeesViewSet


router = routers.DefaultRouter()
router.register(r'^employees', EmployeesViewSet, base_name='api-v1')

urlpatterns = router.urls
