from django.db import models


class Zoxon470GitLabProfile(models.Model):
    username = models.CharField(max_length=125, verbose_name='Логин от GitLab')
    commits_per_day = models.IntegerField(verbose_name='Комиты за день')
    commits_per_week = models.IntegerField(verbose_name='Комиты за неделю')
    commits_per_month = models.IntegerField(verbose_name='Комиты за месяц')

    def __str__(self):
        return self.username
