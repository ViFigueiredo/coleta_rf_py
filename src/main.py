# from services import CriarDiretorios
# from services import ColetarUrls
# from services import ExtractFiles
# from services import MapFiles
# from services import CsvToTable
from services import pyodbc
from services import pymssql

pymssql.test()
pyodbc.test()
# CriarDiretorios.make()
# ColetarUrls.scrape()
# ExtractFiles.extract()
# ExtractFiles.add_extension()
# CsvToTable.insert()
# print(MapFiles.collect())

# TODO: inserção de dados no banco
# TODO: implementar execução automática ou manual
# TODO: migrar as migrations nodejs -> python
