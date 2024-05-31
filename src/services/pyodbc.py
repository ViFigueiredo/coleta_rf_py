import pyodbc

driver_name = '{ODBC Driver 17 for SQL Server}'
server_name = '192.168.0.200,1434\\SQLSERVERFULL'
database_name = 'robo_dados_rf'
username = 'dbAdmin'
password = 'Ctelecom2017'


def test():
    try:
        connection_string = f"""
            DRIVER={driver_name};
            SERVER={server_name};
            DATABASE={database_name};
            UID={username};
            PWD={password};
            Encrypt=no;
        """
        print('Drivers encontrados:', pyodbc.drivers())

        conn = pyodbc.connect(connection_string)
        # print(conn)
        print('Conectado com pyodbc. \n')

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        if sqlstate == '28000':
            print("Acesso negado!")
        else:
            print(f"Erro ao conectar: {ex}")


if __name__ == '__main__':
    test()
