# Projeto de coleta de dados públicos da Receita Federal

- O objetivo é coletar urls de download, salvar localmente arquivos .csv e subí-los porteriormente para um banco de dados relacional.

# Tecnologias utilizadas

- Python (aplicação) com autopep8 (formatação)
- Nodejs (modelagem de banco de dados) com eslint/prettier (formatação e estilização)
- MS SQL Server 2019 (banco de dados relacional)

# Gerar e atualizar libs
pip freeze > requirements.txt

# Instalar libs da aplicação
pip install -r requirements.txt

# Instalar libs para configuração e execução das migrations
npm install

# Executar as migrações (package.json)
npm run migrations