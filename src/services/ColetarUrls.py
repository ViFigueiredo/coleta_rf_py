import requests
from bs4 import BeautifulSoup
import json
import os


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
        for item in mapeamento:
            for item_existente in mapeamento_existente:
                if item["nome_arquivo"] == item_existente["nome_arquivo"]:
                    # Mantém o valor existente para "downloads"
                    item["downloads"] = item_existente["downloads"]
                    item_existente.update(item)
                    break
            else:
                mapeamento_existente.append(item)
        mapeamento = mapeamento_existente

    # Escreva o mapeamento atualizado de volta no arquivo
    with open('./src/mapeamento.json', 'w') as f:
        json.dump(mapeamento, f, indent=4)


if __name__ == '__main__':
    scrape()
