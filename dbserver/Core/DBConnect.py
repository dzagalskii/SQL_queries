import psycopg2
import pyodbc
from .SqlRequestCheck import *
from dbserver.models import AST




def connect_to_postgres():
    sql_request = AST.objects.get(db_index='CQ-2')
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
        cur.execute(
            'SELECT ast1.Code  FROM ASt as ast1 inner join ASt as ast2 on ast1.UPSys = ast2.Code  WHERE ast1.Cost_pm <= ast2.Cost_pm;')
        new_rows = cur.fetchall()
        print(new_rows)
        if rows == new_rows:
            print('ok')
        else:
            find_error(rows, new_rows)

    except Exception:
        print(Exception)

    con.close()


def connect_to_MsSQL():
    sql_request = AST.objects.get(db_index='CQ-2')
    con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                         "Server=DESKTOP-J2U6QDF;"
                         "Database=master;"
                         "Trusted_Connection=yes;")
    cur = con.cursor()
    try:
        cur.execute(sql_request.db_answer)
        rows = cur.fetchall()
        print(rows)
        cur.execute(
            'SELECT ast1.Name  FROM ASt as ast1 inner join ASt as ast2 on ast1.UPSys = ast2.Code  WHERE ast1.Cost_pm <= ast2.Cost_pm;')
        new_rows = cur.fetchall()
        print(new_rows)
        if rows == new_rows:
            print('ok')
        else:
            find_error(rows, new_rows)


    except Exception:
        print(Exception)

    con.close()
