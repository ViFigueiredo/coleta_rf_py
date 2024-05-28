import requests
import json
import os
from PyInquirer import prompt
from tqdm import tqdm  # Importando a biblioteca tqdm para mostrar o progresso


def download():
    # Carregar o mapeamento de arquivos
    with open('./src/mapeamento.json', 'r') as f:
        mapeamento = json.load(f)

    # Certifique-se de que o diretório 'downloads' existe
    os.makedirs('downloads', exist_ok=True)

    # Pergunte ao usuário quais arquivos eles querem baixar
    opcoes_arquivos = [
        {
            'type': 'checkbox',
            'name': 'arquivos',
            'message': 'Selecione os arquivos que você deseja baixar:',
            'choices': [{'name': item['nome_arquivo']} for item in mapeamento]
        }
    ]
    respostas = prompt(opcoes_arquivos)
    arquivos_selecionados = respostas['arquivos']

    # Baixar apenas os arquivos selecionados
    for item in mapeamento:
        nome_arquivo, url = item['nome_arquivo'], item['url']
        if nome_arquivo in arquivos_selecionados:
            # Usando stream=True para download progressivo
            response = requests.get(url, stream=True)
            tamanho_arquivo = int(response.headers.get('content-length', 0))
            caminho_arquivo = f'downloads/{nome_arquivo}'

            # Mostrar o progresso de download com tqdm
            with open(caminho_arquivo, 'wb') as f:
                for data in tqdm(response.iter_content(chunk_size=1024), total=tamanho_arquivo // 1024, unit='KB'):
                    f.write(data)

    print("Download concluído!")


if __name__ == '__main__':
    download()
