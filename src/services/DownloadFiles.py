from PyInquirer import prompt
import requests
import json
import os


def download():
    # Carregar o mapeamento de arquivos
    with open('./src/mapeamento.json', 'r') as f:
        mapeamento = json.load(f)

    # Certifique-se de que o diretório 'downloads' existe
    os.makedirs('downloads', exist_ok=True)

    # Pergunte ao usuário qual opção eles preferem
    opcoes = [
        {
            'type': 'list',
            'name': 'opcao',
            'message': 'Selecione uma das opções abaixo:',
            'choices': ['Download Completo', 'Selecionar arquivo(s)']
        }
    ]
    respostas = prompt(opcoes)
    opcao = respostas['opcao']

    # Baixar cada arquivo
    if opcao == 'Download Completo':
        for item in mapeamento:
            for nome_arquivo, url in item.items():
                response = requests.get(url)
                with open(f'downloads/{nome_arquivo}', 'wb') as f:
                    f.write(response.content)
    elif opcao == 'Selecionar arquivo(s)':
        # Listar os arquivos disponíveis
        opcoes_arquivos = [
            {
                'type': 'checkbox',
                'name': 'arquivos',
                'message': 'Selecione os arquivos que você deseja baixar:',
                'choices': [{'name': nome_arquivo} for item in mapeamento for nome_arquivo in item]
            }
        ]
        respostas = prompt(opcoes_arquivos)
        arquivos_selecionados = respostas['arquivos']

        # Baixar apenas os arquivos selecionados
        for item in mapeamento:
            for nome_arquivo, url in item.items():
                if nome_arquivo in arquivos_selecionados:
                    response = requests.get(url)
                    with open(f'downloads/{nome_arquivo}', 'wb') as f:
                        f.write(response.content)


if __name__ == '__main__':
    download()
