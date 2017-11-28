from django.db import models
from jira.models import JiraProfile
from gitlab.models import GitLabProfile


class Employee(models.Model):
    avatar_url = models.CharField(max_length=255, verbose_name='Avatar')
    jira = models.ForeignKey(JiraProfile, verbose_name='Jira', default=1)
    gitlab = models.ForeignKey(GitLabProfile, verbose_name='GitLab', default=1)

    def __str__(self):
        return 'Employee'
