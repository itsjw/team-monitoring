from rest_framework import viewsets
from jiro.models import JiroProfile
from gitlab.models import GitLabProfile
from user.models import TrackingUser
from api.serializers import JiroProfileSerializer, GitLabProfileSerializer, TrackingUserSerializer



class JiroProfileViewSet(viewsets.ModelViewSet):
    queryset = JiroProfile.objects.all()
    serializer_class = JiroProfileSerializer


class GitLabProfileViewSet(viewsets.ModelViewSet):
    queryset = GitLabProfile.objects.all()
    serializer_class = GitLabProfileSerializer


class TrackingUserViewSet(viewsets.ModelViewSet):
    queryset = TrackingUser.objects.all()
    serializer_class = TrackingUserSerializer
