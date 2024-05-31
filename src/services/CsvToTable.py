import pandas as pd
import pymssql
import os
from dotenv import load_dotenv
from MapFiles import fileToTableMapping


def csv_to_table():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Conexão com o banco de dados
    conn = pymssql.connect(server=os.getenv('DATABASE_HOST') + ':' + os.getenv('DATABASE_PORT'),
                           user=os.getenv('DATABASE_USERNAME'),
                           password=os.getenv('DATABASE_PASSWORD'),
                           database=os.getenv('DATABASE'))

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
