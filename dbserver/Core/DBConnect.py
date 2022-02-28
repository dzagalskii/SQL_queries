import psycopg2
#import cx_Oracle
import pyodbc
from .SqlRequestCheck import *


def filter_query(user_code):
    restricted_words = ['insert', 'delete', 'update', 'create', 'use', 'show', 'source', 'drop', 'describe']
    user_code = user_code.lower()
    for i in restricted_words:
        if (" " + i + " ") in (" " + user_code + " "):
            return -1
    return 0


def check_query(reference_code, user_code, database):
    if filter_query(user_code) == -1:
        return None, "Недопустимый запрос"

    if database == "PG":
        try:
            con = psycopg2.connect(
                database="BoBSDB",
                user="postgres",
                password="postgres",
                host="172.18.0.4",
                port="5432"
            )
        except:
            return None, "Error with DB connection"
    elif database == "MS":
        try:
            con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                 "Server=DESKTOP-J2U6QDF;"
                                 "Database=master;"
                                 "Trusted_Connection=yes;")
        except:
            return None, "Error with DB connection"
    elif database == "Oracle":
        try:
            con = cx_Oracle.connect(
                'username',
                'config.password',
                'config.dsn',
                encoding='UTF-8')

        except:
            return None, "Error with DB connection"
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
            return find_error(reference_output, user_output), None
    except Exception:
        con.close()
        return None, "Exception"
