import requests
import json
import os
from PyInquirer import prompt
from tqdm import tqdm


def convert_to_bytes(file_size):
    size = float(file_size[:-1])
    if 'K' in file_size:
        return size * 1024
    elif 'M' in file_size:
        return size * 1024 * 1024
    elif 'G' in file_size:
        return size * 1024 * 1024 * 1024


def download(baixar_todos=False, baixar_atualizados=False, atualizar=[]):

    # Carregar o mapeamento de arquivos
    with open('./src/mapeamento.json', 'r') as f:
        mapeamento = json.load(f)

    # Ordenar o mapeamento pelo tamanho do arquivo
    mapeamento.sort(key=lambda item: convert_to_bytes(item['fileSize']))

    # Certifique-se de que o diretório 'downloads' existe
    os.makedirs('downloads', exist_ok=True)

    # Se baixar_todos for False e baixar_atualizados for False, pergunte ao usuário quais arquivos eles querem baixar
    if not baixar_todos and not baixar_atualizados:
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
    elif baixar_atualizados:
        # Se baixar_atualizados for True, selecione apenas os arquivos que foram atualizados
        arquivos_selecionados = atualizar
    else:
        arquivos_selecionados = [item['nome_arquivo'] for item in mapeamento]

    # Baixar apenas os arquivos selecionados
    for item in mapeamento:
        nome_arquivo, url = item['nome_arquivo'], item['url']
        if nome_arquivo in arquivos_selecionados:
            caminho_arquivo = f'downloads/{nome_arquivo}'

            # Remover o arquivo se ele já existir
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)

            # Usando stream=True para download progressivo
            response = requests.get(url, stream=True)
            tamanho_arquivo = int(response.headers.get('content-length', 0))

            # Mostrar o progresso de download com tqdm
            with open(caminho_arquivo, 'wb') as f:
                for data in tqdm(response.iter_content(chunk_size=1024), total=tamanho_arquivo // 1024, unit='KB'):
                    f.write(data)

            # Incrementar a contagem de downloads para este arquivo
            item['downloads'] += 1

    print("Atualizados:", atualizar)
    print("Baixados:", arquivos_selecionados)

    # Salvar o mapeamento atualizado
    with open('./src/mapeamento.json', 'w') as f:
        json.dump(mapeamento, f)

    print("Download concluído!")


if __name__ == '__main__':
    download()
