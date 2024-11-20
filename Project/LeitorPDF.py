import os
from PyPDF2 import PdfReader


class LeitorPDF:
    # define o caminho da pasta onde estão os PDFs
    def __init__(self, caminhoPasta):
        self.caminhoPasta = caminhoPasta

    # retorna uma lista com todos os PDFs do diretório
    def listarPdfs(self):
        arquivos_pdf = []
        for arquivo in os.listdir(self.caminhoPasta):
            if arquivo.endswith('.pdf'):
                print(arquivo)  # Exibe cada arquivo PDF encontrado
                arquivos_pdf.append(arquivo)  # Adiciona o arquivo PDF à lista
        return arquivos_pdf

    # Lê e exibe o texto de todos os arquivos PDFs no diretório
    def lerTodosArquivos(self):
        arquivosPdf = self.listarPdfs()  # Obtém a lista de PDFs no diretório
        textosExtraidos = {}  # Dicionário para armazenar textos por arquivo
        
        for nomeArquivo in arquivosPdf:
            caminhoPdf = os.path.join(self.caminhoPasta, nomeArquivo)
            
            # Lê o conteúdo do PDF
            with open(caminhoPdf, 'rb') as arquivoPdf:
                lerPdf = PdfReader(arquivoPdf)
                texto = ""
                
                # Extrai o texto de todas as páginas
                for page in lerPdf.pages:
                    texto += page.extract_text()
            
            # Armazena o texto extraído no dicionário
            textosExtraidos[nomeArquivo] = texto
        
        return textosExtraidos

    # Exibe os textos extraídos de todos os PDFs
    def exibirTextoPdf(self):
        textosExtraidos = self.lerTodosArquivos()
        for nomeArquivo, texto in textosExtraidos.items():
            print('---------------------------------------------------------------------------')
            print(f"Texto do arquivo {nomeArquivo}:\n{texto}\n")
