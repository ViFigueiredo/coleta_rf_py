from services import CriarDiretorios
from services import ColetarUrls
from services import DownloadFiles
from services import ExtractFiles

CriarDiretorios.make()
ColetarUrls.scrape()
DownloadFiles.download()
ExtractFiles.extract()
ExtractFiles.add_extension()

# TODO: implementar remoção de arquivos anteriores antes de baixar e extrair (individual)
# TODO: implementar prioridade de download para arquivo mais leve
# TODO: implementar atualização de mapeamento caso ele já exista
# TODO: implementar migrations e inserção de dados no banco