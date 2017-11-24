from django.db import models


class Zoxon470JiroProfile(models.Model):
    username = models.CharField(max_length=125, verbose_name='Логин от Jira')
    hours_per_day = models.IntegerField(verbose_name='Количество часов за день')
    hours_per_week = models.IntegerField(verbose_name='Количество часов за неделю')
    hours_per_month = models.IntegerField(verbose_name='Количество часов за месяц')

    def __str__(self):
        return self.username