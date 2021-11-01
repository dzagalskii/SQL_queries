from django.http import HttpResponse
from .models import *
from Core.DBConnect import *




def index(request):
    sql_request = AST.objects.get(db_index='CQ-2')
    connect_to_postgres()
    # print(sql_request.db_answer)

    return HttpResponse("Hello, world. You're at the polls index.")
