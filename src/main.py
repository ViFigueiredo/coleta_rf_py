from services import CriarDiretorios
from services import ColetarUrls
from services import DownloadFiles
from services import ExtractFiles

CriarDiretorios.make()
ColetarUrls.scrape()
DownloadFiles.download()
ExtractFiles.extract()
ExtractFiles.add_extension()
