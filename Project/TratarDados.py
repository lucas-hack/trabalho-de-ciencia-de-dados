import re
from LeitorPDF import LeitorPDF 

class TratarDados:
    def __init__(self):
        pass

    # Função para buscar todos os códigos dos clientes, que são códigos de 5 a 6 dígitos 
    def pegarCodigoClientes(self, texto):
        padraoCodigoCliente = r"\b\d{5,6}\b"
        
        codigoCliente = re.findall(padraoCodigoCliente, texto)

        return codigoCliente  
        
    # Função para relacionar o código com um cliente    
    def nomeClienteComCodigo(self, codigoCliente):
        clientes = {
            128831: 'Vortex Solutions',
            127146: 'LumaTech Innovations',
            21300: 'EcoVerde Sustentabilidade',
            126818: 'Alpha Nexa',
            128888: 'Horizonte Digital',
            126454: 'BlueWave Ventures',
            127640: 'InovaBio',
            126702: 'Trilha Solar',
            128883: 'Eclipse Lab',
            128700: 'Mundo Pleno',
            126439: 'Virtualis Consultoria',
            128826: 'Quantum Nexus'
        }
        
        # caso não encontre um usuário, apresenta esta mensagem
        return clientes.get(codigoCliente, "Código de cliente não encontrado")

# instanciada a classe de LeitorPDF
leitor = LeitorPDF("C:/Users/Lucas Hack/Desktop/trabalho de ciência de dados/PDFs/")

# armazenar o que foi encontrado quando lido o PDF
textoPdf = leitor.lerArquivo("OSs38.pdf")


dadosTratados = TratarDados()

codigosClientes = dadosTratados.pegarCodigoClientes(textoPdf)

print("Lista de clientes encontrados:")
for codigo in codigosClientes:
    nomeCliente = dadosTratados.nomeClienteComCodigo(int(codigo))  # Garantir que o código seja um inteiro
    print(f"Código {codigo}: {nomeCliente}")
