from rest_framework import serializers
from jira.models import JiraProfile
from gitlab.models import GitLabProfile
from api.models import Employee


class JiraProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = JiraProfile
        fields = ('id', 'hours_per_day', 'hours_per_week', 'hours_per_month')


class GitLabProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = GitLabProfile
        fields = ('id', 'commits_per_day', 'commits_per_week', 'commits_per_month')


class EmployeeSerializer(serializers.ModelSerializer):
    jira = JiraProfileSerializer(read_only=True)
    gitlab = GitLabProfileSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'username', 'jira', 'gitlab')
