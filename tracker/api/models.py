from django.db import models


class Employees(models.Model):
    username = models.CharField(max_length=35, verbose_name='Username')

    def __str__(self):
        return self.username
