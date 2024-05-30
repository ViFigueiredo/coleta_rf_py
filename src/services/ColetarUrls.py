import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from services import DownloadFiles


def scrape():
    urls = ["https://dados.rfb.gov.br/CNPJ/",
            "https://dados.rfb.gov.br/CNPJ/regime_tributario/"]
    mapeamento = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href.endswith('.zip'):
                nome_arquivo = href.split('/')[-1]
                data_modificacao = link.find_next('td').text.strip()
                tamanho_arquivo = link.find_next(
                    'td').find_next('td').text.strip()
                mapeamento.append({
                    "nome_arquivo": nome_arquivo,
                    "url": url + href,
                    "lastUpdate": data_modificacao,
                    "fileSize": tamanho_arquivo,
                    "downloads": 0,  # Adiciona a chave "downloads" com valor zero
                })

    # Certifique-se de que o diretório src existe
    os.makedirs('./src', exist_ok=True)

    # Verifique se o arquivo mapeamento.json já existe
    if os.path.exists('./src/mapeamento.json'):
        # Se existir, carregue o conteúdo existente
        with open('./src/mapeamento.json', 'r') as f:
            mapeamento_existente = json.load(f)
        # Atualize os campos necessários
        arquivos_atualizados = []
        for item in mapeamento:
            for item_existente in mapeamento_existente:
                if item["nome_arquivo"] == item_existente["nome_arquivo"]:
                    # Mantém o valor existente para "downloads"
                    item["downloads"] = item_existente["downloads"]

                    # Converte as datas para o formato datetime
                    data_existente = datetime.strptime(
                        item_existente["lastUpdate"], "%Y-%m-%d %H:%M")
                    nova_data = datetime.strptime(
                        item["lastUpdate"], "%Y-%m-%d %H:%M")

                    # Se a nova data for mais recente, loga uma mensagem e atualiza a data
                    if nova_data > data_existente:
                        print(
                            f"O arquivo {item['nome_arquivo']} foi atualizado em {item['lastUpdate']}")
                        item_existente["lastUpdate"] = item["lastUpdate"]
                        arquivos_atualizados.append(item['nome_arquivo'])

                    # Atualiza os outros campos
                    item_existente["url"] = item["url"]
                    item_existente["fileSize"] = item["fileSize"]
                    break
            else:
                mapeamento_existente.append(item)
        mapeamento = mapeamento_existente

    # Escreva o mapeamento atualizado de volta no arquivo
    with open('./src/mapeamento.json', 'w') as f:
        json.dump(mapeamento, f, indent=4)

    # Pergunte ao usuário se ele deseja baixar todos os arquivos, selecionar quais arquivos baixar ou apenas os atualizados
    escolha = input(
        "Você deseja baixar todos os arquivos, selecionar quais arquivos baixar ou apenas atualizar? (1 - Tudo / 2 - Selecionar / 3 - Atualizar): ")

    if escolha == "1":
        # Chame a função para baixar todos os arquivos
        DownloadFiles.download(baixar_todos=True)
    elif escolha == "2":
        # Chame a função para selecionar e baixar arquivos específicos
        DownloadFiles.download(baixar_todos=False)
    elif escolha == "3":
        # Chame a função para baixar apenas os arquivos atualizados
        DownloadFiles.download(
            baixar_todos=False, baixar_atualizados=True, atualizar=arquivos_atualizados)
    else:
        print("Escolha inválida. Por favor, escolha '1' para Tudo, '2' para Selecionar, ou '3' para Atualizar.")


if __name__ == '__main__':
    scrape()
