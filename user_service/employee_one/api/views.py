from rest_framework import viewsets
from jira.models import JiraProfile
from gitlab.models import GitLabProfile
from api.models import Employee
from api.serializers import JiraProfileSerializer, GitLabProfileSerializer, EmployeeSerializer


class JiraProfileViewSet(viewsets.ModelViewSet):
    queryset = JiraProfile.objects.all()
    serializer_class = JiraProfileSerializer


class GitLabProfileViewSet(viewsets.ModelViewSet):
    queryset = GitLabProfile.objects.all()
    serializer_class = GitLabProfileSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()[:1]
    serializer_class = EmployeeSerializer
