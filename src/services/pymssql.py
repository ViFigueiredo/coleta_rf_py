import pymssql

driver_name = '{ODBC Driver 18 for SQL Server}'
server_name = '192.168.0.200\SQLSERVERFULL'
database_name = 'robo_dados_rf'
username = 'dbAdmin'
password = 'Ctelecom2017'


def connection():

    try:
        conn = pymssql.connect(
            server=server_name,
            user=username,
            password=password,
            database=database_name)
        print('[DB] -> Conectado com sucesso!. \n')
        return conn
    except Exception as e:
        print("[DB] -> Falha na conexão: \n", e)


if __name__ == '__main__':
    connection()
