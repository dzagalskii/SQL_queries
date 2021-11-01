import psycopg2
from SqlRequestCheck import *

def connect_to_postgres():

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
