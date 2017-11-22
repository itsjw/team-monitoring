from django.db import models
from django.contrib.auth.models import AbstractUser
from jiro.models import Zoxon470JiroProfile
from gitlab.models import Zoxon470GitLabProfile


class Zoxon470TrackingUser(AbstractUser):
    avatar_url = models.CharField(max_length=255, verbose_name='Аватар')
    jiro = models.ForeignKey(Zoxon470JiroProfile, verbose_name='Jiro', default=1)
    gitlab = models.ForeignKey(Zoxon470GitLabProfile, verbose_name='GitLab', default=1)

    def __str__(self):
        return self.username