from rest_framework import viewsets
from api.models import Employees
from api.serializers import EmployeesSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
