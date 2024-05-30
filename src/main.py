from services import CriarDiretorios
from services import ColetarUrls
from services import ExtractFiles

CriarDiretorios.make()
ColetarUrls.scrape()
ExtractFiles.extract()
ExtractFiles.add_extension()

# TODO: implementar atualização de mapeamento caso ele já exista
# TODO: implementar migrations e inserção de dados no banco
# TODO: implementar execução automática ou manual