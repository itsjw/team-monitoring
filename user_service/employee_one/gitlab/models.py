from django.db import models


class GitLabProfile(models.Model):
    username = models.CharField(max_length=125, verbose_name='Username from Gitlab')
    commits_per_day = models.IntegerField(verbose_name='Commits per day')
    commits_per_week = models.IntegerField(verbose_name='Commits per week')
    commits_per_month = models.IntegerField(verbose_name='Commits per month')

    def __str__(self):
        return self.username
