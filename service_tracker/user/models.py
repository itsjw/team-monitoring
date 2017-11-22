from django.db import models
from django.contrib.auth.models import AbstractUser
from jiro.models import JiroProfile
from gitlab.models import GitLabProfile


class TrackingUser(AbstractUser):
    avatar_url = models.CharField(max_length=255, verbose_name='Аватар')
    jiro = models.ForeignKey(JiroProfile, verbose_name='Jiro', default=1)
    gitlab = models.ForeignKey(GitLabProfile, verbose_name='GitLab', default=1)

    def __str__(self):
        return self.username