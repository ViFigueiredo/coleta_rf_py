import os
import re


def collect():
    pasta = 'extracted'
    strings_coletadas = []

    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.csv'):
            match = re.search(r'(?:.*\.)?(.*)\.csv$', nome_arquivo)
            if match:
                string_coletada = match.group(1)
                # Removendo o ano se o nome do arquivo começa com "Lucro"
                if string_coletada.startswith('Lucro'):
                    string_coletada = re.sub(r'\d+', '', string_coletada)
                # Removendo espaços extras
                string_coletada = string_coletada.strip()
                strings_coletadas.append(string_coletada)

    # Removendo duplicatas
    strings_coletadas = list(set(strings_coletadas))

    return strings_coletadas


# Mapeamento de arquivos para o banco de dados
def fileToTableMapping():
    return {
        'CNAECSV': {
            'table': 'cnaes',
            'collumns': ['codigo', 'descricao'],
        },
        'SIMPLES': {
            'table': 'dados-simples',
            'collumns': [
                'cnpj_basico',
                'opcao_simples',
                'data_opcao_simples',
                'data_exclusao_simples',
                'opcao_mei',
                'data_opcao_mei',
                'data_exclusao_mei',
            ],
        },
        'EMPRECSV': {
            'table': 'empresas',
            'collumns': [
                'cnpj_basico',
                'razao_social',
                'natureza_juridica',
                'qualificacao_responsavel',
                'capital_social',
                'porte_empresa',
                'ente_federativo',
            ],
        },
        'ESTABELE': {
            'table': 'estabelecimentos',
            'collumns': [
                'cnpj_basico',
                'cnpj_ordem',
                'cnpj_dv',
                'identificador_matriz_filial',
                'nome_fantasia',
                'situacao_cadastral',
                'motivo_situacai_cadastral',
                'nome_cidade_exterior',
                'pais',
                'data_inicio_atividade',
                'cnae_fiscal_principal',
                'cnae_fiscal_secundaria',
                'tipo_logradouro',
                'logradouro',
                'numero',
                'complemento',
                'bairro',
                'cep',
                'uf',
                'municipio',
                'ddd1',
                'telefone1',
                'ddd2',
                'telefone2',
                'ddd_fax',
                'fax',
                'correio_eletronico',
                'situacao_especial',
                'data_situacao_especial',
            ],
        },
        'MOTIVCSV': {
            'table': 'motivos',
            'collumns': ['codigo', 'descricao'],
        },
        'MUNICCSV': {
            'table': 'municipios',
            'collumns': ['codigo', 'descricao'],
        },
        'NATJUCSV': {
            'table': 'naturezas-juridicas',
            'collumns': ['codigo', 'descricao'],
        },
        'PAISCSV': {
            'table': 'paises',
            'collumns': ['codigo', 'descricao'],
        },
        'QUALSCSV': {
            'table': 'qualificacao-socios',
            'collumns': ['codigo', 'descricao'],
        },
        'SOCIOCSV': {
            'table': 'socios',
            'collumns': [
                'cnpj_basico',
                'identificador_socio',
                'nome_razao_socio',
                'documento_socio',
                'qualificacao_socio',
                'data_entrada_sociedade',
                'pais',
                'representante_legal',
                'nome_representante',
                'qualificacao_representante_legal',
                'faixa_etaria',
            ],
        },
        'Imunes e isentas': {
            'table': 'imunes-isentas',
            'collumns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        },
        'Lucro Arbitrado': {
            'table': 'lucro-arbitrado',
            'collumns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        },
        'Lucro Presumido': {
            'table': 'lucro-presumido',
            'collumns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        },
        'Lucro Real': {
            'table': 'lucro-real',
            'collumns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        }
    }


if __name__ == '__main__':
    collect()
    fileToTableMapping()
