import os
import zipfile


def extract():
    # Certifique-se de que o diretório 'extracted' existe
    os.makedirs('extracted', exist_ok=True)

    # Percorra todos os arquivos no diretório 'downloads'
    for filename in os.listdir('downloads'):
        if filename.endswith('.zip'):
            # Crie um objeto ZipFile
            with zipfile.ZipFile(f'downloads/{filename}', 'r') as zip_ref:
                # Extraia todos os arquivos para o diretório 'extracted'
                for member in zip_ref.namelist():
                    path = os.path.join('extracted', member + '.csv')
                    # Remover o arquivo se ele já existir
                    if os.path.exists(path):
                        os.remove(path)
                    zip_ref.extract(member, 'extracted')


def add_extension():
    # Percorra todos os arquivos no diretório 'extracted'
    for filename in os.listdir('extracted'):
        # Se o arquivo não tem a extensão .csv, adicione-a
        if not filename.endswith('.csv'):
            os.rename(f'extracted/{filename}', f'extracted/{filename}.csv')


if __name__ == '__main__':
    extract()
    add_extension()
