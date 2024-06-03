import os
import re


# Mapeamento de arquivos para o banco de dados
def fileToTableMapping():
    return {
        'CNAECSV': {
            'table': 'cnaes',
            'columns': ['codigo', 'descricao'],
        },
        'SIMPLES': {
            'table': 'dados-simples',
            'columns': [
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
            'columns': [
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
            'columns': [
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
            'columns': ['codigo', 'descricao'],
        },
        'MUNICCSV': {
            'table': 'municipios',
            'columns': ['codigo', 'descricao'],
        },
        'NATJUCSV': {
            'table': 'naturezas-juridicas',
            'columns': ['codigo', 'descricao'],
        },
        'PAISCSV': {
            'table': 'paises',
            'columns': ['codigo', 'descricao'],
        },
        'QUALSCSV': {
            'table': 'qualificacao-socios',
            'columns': ['codigo', 'descricao'],
        },
        'SOCIOCSV': {
            'table': 'socios',
            'columns': [
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
            'columns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        },
        'Lucro Arbitrado': {
            'table': 'lucro-arbitrado',
            'columns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        },
        'Lucro Presumido': {
            'table': 'lucro-presumido',
            'columns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        },
        'Lucro Real': {
            'table': 'lucro-real',
            'columns': ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
        }
    }


if __name__ == '__main__':
    fileToTableMapping()
