import pandas as pd
import os
import sys
from dotenv import load_dotenv
from MapFiles import fileToTableMapping

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def insert():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Conexão com o banco de dados
    conn = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.200\\sqlserverfull;PORT=1434;DATABASE=robo_dados_rf;UID=dbAdmin;PWD=Ctelecom2017'

    cursor = conn.cursor()

    # Mapeamento de arquivos para tabelas
    mapping = fileToTableMapping()

    # Diretório dos arquivos CSV
    dir_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), '..', 'extracted')

    for file_name, table_info in mapping.items():
        # Leitura do arquivo CSV
        df = pd.read_csv(os.path.join(dir_path, file_name))

        # Inserção dos dados na tabela
        for index, row in df.iterrows():
            placeholders = ', '.join(['%s'] * len(row))
            columns = ', '.join(table_info['columns'])
            sql = f"INSERT INTO {table_info['table']} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(row))

    # Commit das alterações
    conn.commit()

    # Mensagem de log
    print("Inserção de dados concluída com sucesso!")


if __name__ == '__main__':
    insert()
