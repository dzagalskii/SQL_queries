from django.db import models
from django.conf import settings


class ControlWork(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_query_answer = models.CharField(max_length=1000)
    second_query_answer = models.CharField(max_length=1000)
    third_query_answer = models.CharField(max_length=1000)

