import os
import pandas as pd
from tqdm import tqdm
from services import pymssql
from services import MapFiles


def load_csv_to_db(file_path, table_name, columns, conn):
    # Carregar dados do arquivo CSV
    # Verificar se o arquivo é 'Lucro Arbitrado'
    if 'Lucro Arbitrado' or 'Lucro Real' in file_path:
        data = pd.read_csv(file_path, header=None, names=columns,
                           sep=',', encoding='latin1', skiprows=1)
    else:
        data = pd.read_csv(file_path, header=None,
                           names=columns, sep=';', encoding='latin1')

    # Criar cursor
    cursor = conn.cursor()

    # Iniciar uma transação
    cursor.execute("BEGIN TRANSACTION")

    # Preparar a string de inserção
    insert_str = f"INSERT INTO [{table_name}] ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

    # Iterar sobre as linhas do dataframe e inserir no banco de dados
    for index, row in tqdm(data.iterrows(), total=data.shape[0], desc=f'Inserindo {file_path}'):
        cursor.execute(insert_str, tuple(row))

    # Confirmar a transação
    cursor.execute("COMMIT TRANSACTION")


def process_files():
    # Obter a conexão ao banco de dados
    conn = pymssql.connection()

    # Obter o mapeamento de arquivos para tabelas
    mapping = MapFiles.fileToTableMapping()

    # Iterar sobre todos os arquivos na pasta extraída
    for file_name in os.listdir('./extracted'):
        # Verificar se o nome do arquivo existe no mapeamento
        for key in mapping.keys():
            if key in file_name:
                # Obter o nome da tabela e as colunas
                table_name = mapping[key]['table']
                columns = mapping[key]['columns']

                # Carregar o arquivo CSV para o banco de dados
                load_csv_to_db(
                    f'./extracted/{file_name}', table_name, columns, conn)


if __name__ == '__main__':
    process_files()
