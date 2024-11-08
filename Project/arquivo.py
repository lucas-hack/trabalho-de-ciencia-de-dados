import os
from PyPDF2 import PdfReader


class LeitorPDF:
    # define o caminho da pasta onde está os PDFs
    def __init__(self, caminhoPasta):
        self.caminhoPasta = caminhoPasta

    # retorna uma lista com todos os PDFs do diretório
    def listarPdfs(self):
        return[arquivo for arquivo in os.listdir(self.caminhoPasta) if arquivo.endswith('.pdf')]
    
    # Lê o conteúdo dos arquivos
    def lerArquivo(self, nomeArquivo):
        caminhoPdf = os.path.join(self.caminhoPasta, nomeArquivo)
        with open(caminhoPdf, 'rb') as arquivoPdf:
            lerPdf = PdfReader(arquivoPdf)
            
            # Acessa e extrai texto da primeira página (ou faça um loop para várias páginas)
            page = lerPdf.pages[0]
            text = page.extract_text()
        return text
    
    # exibe o texto que se encontra na página
    def exibirTextoPdf(self):
        arquivoPdf = self.listarPdfs()
        for nomeArquivo in arquivoPdf:
            text = self.lerArquivo(nomeArquivo)
            print('---------------------------------------------------------------------------')
            print(f"Texto do arquivo {nomeArquivo}:\n{text}\n")

caminhoDaPasta = 'C:/Users/Lucas Hack/Desktop/trabalho de ciência de dados/PDFs/'

leitor = LeitorPDF(caminhoDaPasta)

leitor.exibirTextoPdf()
