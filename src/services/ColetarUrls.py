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
                mapeamento.append({nome_arquivo: url + href})

    # Certifique-se de que o diretório src existe
    os.makedirs('./src', exist_ok=True)

    with open('./src/mapeamento.json', 'w') as f:
        json.dump(mapeamento, f, indent=4)


if __name__ == '__main__':
    scrape()
