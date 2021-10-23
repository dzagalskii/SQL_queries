import psycopg2
from django.http import HttpResponse
from .models import *
from django.shortcuts import render


# Create your views here.

def index(request):
    sql_request = AST.objects.get(db_index='CQ-2')
    #print(sql_request.db_answer)
    con = psycopg2.connect(
        database="BoBSDB",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    try:
        cur.execute(sql_request.db_answer)
        rows = cur.fetchall()
        print(rows)
        cur.execute('SELECT ast1.Name  FROM ASt as ast1 inner join ASt as ast2 on ast1.UPSys = ast2.Code  WHERE ast1.Cost_pm <= ast2.Cost_pm;')
        new_rows = cur.fetchall()
        print(new_rows)
        if rows == new_rows:
            print('ok')
        else:
            print('not ok')


    except Exception:
        print(Exception)


    con.close()

    return HttpResponse("Hello, world. You're at the polls index.")
