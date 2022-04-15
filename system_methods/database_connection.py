from peewee import MySQLDatabase, SqliteDatabase


def make_connect():

    sql_db = SqliteDatabase('cds_database.db')
                         

    return sql_db()




""" 

MYSQL_USERNAME = 'cds_integracao'
MYSQL_PASS = '123'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306

def make_connect():

    mysql_db = MySQLDatabase(
                        'CDS_API',
                         user=MYSQL_USERNAME,
                         password=MYSQL_PASS,
                         host=MYSQL_HOST,
                         port=MYSQL_PORT
                         )

    return mysql_db()

"""


