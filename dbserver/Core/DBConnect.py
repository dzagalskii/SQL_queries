import psycopg2
import pyodbc
from .SqlRequestCheck import *


def check_query(reference_code, user_code, database):
    # TODO: ПЕРЕНЕСТИ ПАРАМЕТРЫ В SETTINGS
    if database == "PG":
        con = psycopg2.connect(
            database="bobsdb",
            user="postgres",
            password="0512",
            host="127.0.0.1",
            port="5432"
        )
    elif database == "MS":
        con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                             "Server=DESKTOP-J2U6QDF;"
                             "Database=master;"
                             "Trusted_Connection=yes;")
    else:
        return None, "Unknown database"
    cur = con.cursor()
    try:
        cur.execute(reference_code)
        reference_output = cur.fetchall()

        cur.execute(user_code)
        user_output = cur.fetchall()

        con.close()

        if reference_output == user_output:
            return "OK", None
        else:
            return find_error(reference_output, reference_output), None
    except Exception:
        return None, "Exception"

