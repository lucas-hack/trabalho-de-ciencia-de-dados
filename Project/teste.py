from LeitorPDF import LeitorPDF 
from TratarDados import TratarDados

# Instanciando a classe LeitorPDF
leitor = LeitorPDF("C:/Users/Lucas Hack/Desktop/trabalho de ciência de dados/PDFs")

# Armazenando o que foi encontrado quando lido o PDF
textoPdf = leitor.lerArquivo("OSs38.pdf")

# Instância da classe TratarDados
dadosTratados = TratarDados()

# Chamando a função mostrarDadosTratados com o texto extraído do PDF
dadosTratados.mostrarDadosTratados(textoPdf)

