def init_db():
    try:
        postgres_con = psycopg2.connect(
            database="BoBSDB",
            user="postgres",
            password="postgres",
            host="10.1.0.100",
            port="5432")
    except Exception as e:
        print("Error with DB connection: {}".format(e))
        return

    try:
        mssql_con = pyodbc.connect("DRIVER={FreeTDS};"
                                   "SERVER=mssql_container;"
                                   "PORT=1433;"
                                   "DATABASE=master;"
                                   "UID=sa;"
                                   "PWD=Secret1234")
    except Exception as e:
        print("Error with DB connection: {}".format(e))
        return

    postgres_cur = postgres_con.cursor()
    mssql_cur = mssql_con.cursor()

    try:
        postgres_init_file = open('config/postgres/init_db.sql')
        mssql_init_file = open('config/ms/init_db.sql')

        postgres_init_script = postgres_init_file.read()
        mssql_init_script = mssql_init_file.read()

        postgres_cur.execute(postgres_init_script)
        mssql_cur.execute(mssql_init_script)

        postgres_con.close()
        cmssql_conon.close()

    except Exception as e:
        postgres_con.close()
        cmssql_conon.close()
        print("Error with DB initialization: {}".format(e))
        return


if __name__ == "__main__":
    init_db()