import psycopg2
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
                host="10.1.0.100",
                port="5432"
            )
        except Exception as e:
            return None, "Ошибка подключения к базе данных PG: {}".format(e)
    elif database == "MS":
        try:
            con = pyodbc.connect("DRIVER={FreeTDS};"
                                 "SERVER=mssql_container;"
                                 "PORT=1433;"
                                 "DATABASE=master;"
                                 "UID=sa;"
                                 "PWD=Secret1234")
        except Exception as e:
            return None, "Ошибка подключения к базе данных MS: {}".format(e)
    else:
        return None, "Неизвестная база данных..."

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
    except Exception as e:
        con.close()
        print('Возникла при выполнении запроса, проверьте синтаксис: {}'.format(e))
        return None, 'Возникла при выполнении запроса, проверьте синтаксис'
