from rest_framework import serializers
from jiro.models import Zoxon470JiroProfile
from gitlab.models import Zoxon470GitLabProfile
from user.models import Zoxon470TrackingUser


class JiroProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zoxon470JiroProfile
        fields = ('id', 'hours_per_day', 'hours_per_week', 'hours_per_month')


class GitLabProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zoxon470GitLabProfile
        fields = ('id', 'commits_per_day', 'commits_per_week', 'commits_per_month')


class TrackingUserSerializer(serializers.ModelSerializer):
    jiro = JiroProfileSerializer(read_only=True)
    gitlab = GitLabProfileSerializer(read_only=True)

    class Meta:
        model = Zoxon470TrackingUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'avatar_url', 'jiro', 'gitlab')
