from django.db import models


class JiraProfile(models.Model):
    username = models.CharField(max_length=125, verbose_name='Username from Jira')
    hours_per_day = models.IntegerField(verbose_name='Hours per day')
    hours_per_week = models.IntegerField(verbose_name='Hours per week')
    hours_per_month = models.IntegerField(verbose_name='Hours per month')

    def __str__(self):
        return self.username
