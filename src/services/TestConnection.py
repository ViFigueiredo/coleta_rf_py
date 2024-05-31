import pyodbc
from dotenv import load_dotenv
import os


def test():
    load_dotenv()

    try:

        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                       'SERVER=' + os.getenv('DATABASE_HOST') + ';'
                       'DATABASE=' + os.getenv('DATABASE') + ';'
                       'UID=' + os.getenv('DATABASE_USERNAME') + ';'
                       'PWD=' + os.getenv('DATABASE_PASSWORD'))
        print("Conexão bem-sucedida!")
    except pyodbc.Error as ex:
        print("Falha na conexão:", ex)


if __name__ == '__main__':
    test()
