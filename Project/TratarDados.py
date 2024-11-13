import re

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
    
    # Função para contar as ocorrências de cada tipo de serviço
    def contarTiposServico(self, texto):
        # Definimos os padrões de serviço
        padraoSolicitacao = 'INT-SOLICITAÇÃO'
        padraoRetrabalho = 'ATR-RETRABALHO P'
        
        # Conta as ocorrências de cada tipo de serviço
        contagem_solicitacao = len(re.findall(padraoSolicitacao, texto))
        contagem_retrabalho = len(re.findall(padraoRetrabalho, texto))

        return {
            'INT-SOLICITAÇÃO': contagem_solicitacao,
            'ATR-RETRABALHO P': contagem_retrabalho
        }

    # Função para exibir os dados tratados
    def mostrarDadosTratados(self, texto):
        # Extrair códigos de cliente do texto
        codigosClientes = self.pegarCodigoClientes(texto)
        print("Códigos de clientes e nomes correspondentes:")

        # Exibir o nome de cada cliente usando o código extraído
        for codigo in codigosClientes:
            nomeCliente = self.nomeClienteComCodigo(int(codigo))
            print(f"Código {codigo}: {nomeCliente}")
        
        # Contar e exibir os tipos de serviço
        tipos_servico = self.contarTiposServico(texto)
        print("\nContagem de tipos de serviço:")
        for tipo, contagem in tipos_servico.items():
            print(f"{tipo}: {contagem}")

        print("Texto original:", texto)
        print("Ocorrências de 'INT-SOLICITAÇÃO':", texto.count('INT-SOLICITAÇÃO'))
        print("Ocorrências de 'ATR-RETRABALHO P':", texto.count('ATR-RETRABALHO P'))

