const path = require('path');
const fs = require('fs');
const knex = require('../config/knex');
const csvParser = require('csv-parser');
const iconv = require('iconv-lite');

async function testConnection() {
  try {
    await knex.raw('select 1+1 as result');
    console.log('Conexão com o banco de dados estabelecida com sucesso!');
  } catch (err) {
    console.error('Erro ao conectar com o banco de dados:', err);
  }
}

const fileToTableMapping = {
  CNAECSV: {
    table: 'cnaes',
    collumns: ['codigo', 'descricao'],
  },
  SIMPLES: {
    table: 'dados-simples',
    collumns: [
      'cnpj_basico',
      'opcao_simples',
      'data_opcao_simples',
      'data_exclusao_simples',
      'opcao_mei',
      'data_opcao_mei',
      'data_exclusao_mei',
    ],
  },
  EMPRECSV: {
    table: 'empresas',
    collumns: [
      'cnpj_basico',
      'razao_social',
      'natureza_juridica',
      'qualificacao_responsavel',
      'capital_social',
      'porte_empresa',
      'ente_federativo',
    ],
  },
  ESTABELE: {
    table: 'estabelecimentos',
    collumns: [
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
  MOTIVCSV: {
    table: 'motivos',
    collumns: ['codigo', 'descricao'],
  },
  MUNICCSV: {
    table: 'municipios',
    collumns: ['codigo', 'descricao'],
  },
  NATJUCSV: {
    table: 'naturezas-juridicas',
    collumns: ['codigo', 'descricao'],
  },
  PAISCSV: {
    table: 'paises',
    collumns: ['codigo', 'descricao'],
  },
  QUALSCSV: {
    table: 'qualificacao-socios',
    collumns: ['codigo', 'descricao'],
  },
  SOCIOCSV: {
    tabl: 'socios',
    collumns: [
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
    table: 'imunes-isentas',
    collumns: ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
  },
  'Lucro Arbitrado': {
    table: 'lucro-arbitrado',
    collumns: ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
  },
  'Lucro Presumido': {
    table: 'lucro-presumido',
    collumns: ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
  },
  'Lucro Real': {
    table: 'lucro-real',
    collumns: ['ano', 'cnpj', 'cnpj_scp', 'forma_tributacao', 'quantidade_escrituracoes'],
  },
};

async function InsertDataDB() {
  // Caminho para a pasta "extracted"
  const directoryPath = path.join(__dirname, '../../extracted');

  // Define o tamanho do lote
  const batchSize = 20000;

  // Define os delimitadores possíveis
  const delimiters = [',', ';'];

  // Lê todos os arquivos na pasta "extracted"
  fs.readdir(directoryPath, async (err, files) => {
    if (err) {
      return console.error('Erro ao ler o diretório:', err);
    }

    // Itera sobre cada arquivo
    for (const file of files) {
      // Encontra a chave correspondente no mapeamento
      const key = Object.keys(fileToTableMapping).find((key) => file.includes(key));

      if (key) {
        const { table, collumns } = fileToTableMapping[key];
        let count = 0;

        // Log do arquivo que está sendo lido
        console.log(`Processando o arquivo: ${file}`);

        // Itera sobre cada delimitador possível
        for (const delimiter of delimiters) {
          // Cria um array para armazenar as linhas
          const rows = [];

          // Cria um stream de leitura para o arquivo .csv
          const stream = fs
            .createReadStream(path.join(directoryPath, file))
            .pipe(iconv.decodeStream('iso-8859-1'))
            .pipe(csvParser({ delimiter }));

          // Itera sobre cada linha do arquivo .csv
          for await (const row of stream) {
            // Adiciona a linha ao array
            rows.push(collumns.reduce((obj, col) => ({ ...obj, [col]: row[col] }), {}));
            count++;

            // Se o array atingir o tamanho do lote, insere no banco de dados e limpa o array
            if (count % batchSize === 0) {
              try {
                await knex.batchInsert(table, rows);
                rows.length = 0; // Limpa o array
              } catch (err) {
                console.error('Erro ao inserir linhas no banco de dados:', err);
              }
            }
          }

          // Insere quaisquer linhas restantes que não chegaram ao tamanho do lote
          if (rows.length > 0) {
            try {
              await knex.batchInsert(table, rows);
              count += rows.length;
            } catch (err) {
              console.error('Erro ao inserir linhas no banco de dados:', err);
            }
          }

          // Se alguma linha foi inserida, interrompe a iteração dos delimitadores
          if (count > 0) {
            break;
          }
        }

        // Log da inserção de linhas no banco de dados
        console.log(`Inseridas ${count} linhas na tabela ${table} a partir do arquivo ${file}`);
      }
    }
  });
}

testConnection()
  .then(() => {
    InsertDataDB();
  })
  .catch(() => {
    console.log('Falha na inserção de dados.');
  });
