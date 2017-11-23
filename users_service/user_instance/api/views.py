from rest_framework import viewsets
from jiro.models import Zoxon470JiroProfile
from gitlab.models import Zoxon470GitLabProfile
from user.models import Zoxon470TrackingUser
from api.serializers import JiroProfileSerializer, GitLabProfileSerializer, TrackingUserSerializer



class JiroProfileViewSet(viewsets.ModelViewSet):
    queryset = Zoxon470JiroProfile.objects.all()[:1]
    serializer_class = JiroProfileSerializer


class GitLabProfileViewSet(viewsets.ModelViewSet):
    queryset = Zoxon470GitLabProfile.objects.all()[:1]
    serializer_class = GitLabProfileSerializer


class TrackingUserViewSet(viewsets.ModelViewSet):
    queryset = Zoxon470TrackingUser.objects.all()[:1]
    serializer_class = TrackingUserSerializer
