from services import CriarDiretorios
from services import ColetarUrls
from services import ExtractFiles

async def main():
  CriarDiretorios.make()
  ColetarUrls.scrape()
  ExtractFiles.extract()
  ExtractFiles.add_extension()

# TODO: inserção de dados no banco
# TODO: implementar execução automática e manual
# TODO: migrar as migrations nodejs -> python
