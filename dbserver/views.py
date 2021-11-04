from django.http import HttpResponse
from .models import *
from .Core.DBConnect import *


def index(request):
    connect_to_MsSQL()
    # print(sql_request.db_answer)

    return HttpResponse("Hello, world. You're at the polls index.")
