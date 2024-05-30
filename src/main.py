from services import CriarDiretorios
from services import ColetarUrls
from services import ExtractFiles
from services import MapFiles

CriarDiretorios.make()
ColetarUrls.scrape()
ExtractFiles.extract()
ExtractFiles.add_extension()
# print(MapFiles.collect())

# TODO: implementar migrations e inserção de dados no banco
# TODO: implementar execução automática ou manual
