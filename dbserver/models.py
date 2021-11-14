from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DataScheme(models.Model):
    scheme_name = models.CharField(max_length=10)
    image_path = models.ImageField(upload_to='static')

    def __str__(self):
        return f"Name:{self.scheme_name}\n"


class ControlWork(models.Model):
    control_name = models.CharField(max_length=100)
    control_desc = models.CharField(max_length=200)
    control_scheme = models.OneToOneField(DataScheme, on_delete=models.CASCADE, related_name='control_work')

    def __str__(self):
        return f"Name:{self.control_name}\n"


class Query(models.Model):
    # db_index = models.CharField(max_length=10)
    query_request = models.CharField(max_length=250)
    query_answer = models.CharField(max_length=250)
    query_scheme = models.ForeignKey(DataScheme, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return f"Index:{self.query_request}\n"


class ExecControlWork(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    control_work = models.ForeignKey(ControlWork, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    query_1 = models.OneToOneField(Query, on_delete=models.CASCADE, related_name='query_1')
    query_2 = models.OneToOneField(Query, on_delete=models.CASCADE, related_name='query_2')
    query_3 = models.OneToOneField(Query, on_delete=models.CASCADE, related_name='query_3')
    query_1_answer = models.CharField(max_length=250)
    query_2_answer = models.CharField(max_length=250)
    query_3_answer = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"User: {self.user.username}\n" \
               f"Control work: {self.control_work}\n"


class AST(models.Model):
    db_index = models.CharField(max_length=10)
    db_request = models.CharField(max_length=250)
    db_answer = models.CharField(max_length=250)

    def __str__(self):
        return f"Index:{self.db_index}\n"
