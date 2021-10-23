from django.db import models


# Create your models here.
class AST(models.Model):
    db_index = models.CharField(max_length=10)
    db_request = models.CharField(max_length=250)
    db_answer = models.CharField(max_length=250)

    def __str__(self):
        return f"Index:{self.db_index}\n"


