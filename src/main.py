from services import CriarDiretorios
from services import ColetarUrls
from services import ExtractFiles
from services import InsertFiles

CriarDiretorios.make()
ColetarUrls.scrape()
ExtractFiles.extract()
ExtractFiles.add_extension()
InsertFiles.process_files()

# TODO: inserção de dados no banco
# TODO: implementar execução automática ou manual
# TODO: migrar as migrations nodejs -> python
