import re
from LeitorPDF import LeitorPDF
from Desenvolvedores import Desenvolvedores

# é feita uma herança para pegar todos os métodos de LeitorPDF
class TratarDados(LeitorPDF):
    def __init__(self, caminhoPasta):
        super().__init__(caminhoPasta)
        self.desenvolvedores = Desenvolvedores()

    # Função para buscar todos os códigos dos clientes
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
            128826: 'Quantum Nexus',
            49222: 'Nova Era Consultoria',
            127901: 'Pinnacle Systems',
            127420: 'Atlas Dynamics Group',
            127733: 'Nexa Prime Solutions',
            126624: 'Aurum Tech Solutions',
            126559: 'BrightPath Enterprises',
            126720: 'Horizon Wave Industries',
            126746: 'Quantum Crest Innovations',
            126497: 'Vertex Alliance',
            127939: 'EvoLogic Systems',
            127065: 'PolarStream Technologies',
            127562: 'Skybridge Ventures',
            127770: 'InovaEdge Labs',
            126425: 'BlueNova Solutions',
            128673: 'EcoSphere Innovations',
            126531: 'NextPhase Consulting',
            127673: 'TrueVantage Tech',
            127912: 'Alpha Horizon Systems',
            127566: 'Luminary Nexus Solutions'
        }
        # caso não encontre um usuário, apresenta esta mensagem
        return clientes.get(codigoCliente, "Código de cliente não encontrado")
    
    def contarNomesDesenvolvedores(self, texto):
        # Obtemos o dicionário de desenvolvedores
        nomes_map = self.desenvolvedores.listarDesenv()

        # Criamos um dicionário para armazenar as contagens
        contagem_nomes = {nome: 0 for nome in nomes_map.values()}

        # Contamos a ocorrência de cada nome no texto
        for nome_chave, nome_real in nomes_map.items():
            contagem_nomes[nome_real] += len(re.findall(rf'\b{nome_chave}\b', texto))

        return contagem_nomes

    # Listagem de frequência de nomes em cada arquivo PDF
    def listarFrequenciaNomesPorArquivo(self):
        textosExtraidos = self.lerTodosArquivos()  # Lê o conteúdo de todos os PDFs
        resultados = {}

        for nomeArquivo, texto in textosExtraidos.items():
            contagem_nomes = self.contarNomesDesenvolvedores(texto)
            resultados[nomeArquivo] = contagem_nomes

        return resultados

    # Exibe os dados de frequência de nomes
    def mostrarFrequenciaNomes(self):
        resultados = self.listarFrequenciaNomesPorArquivo()
        for nomeArquivo, contagem_nomes in resultados.items():
            print(f"\nFrequência de nomes no arquivo {nomeArquivo}:")
            for nome, frequencia in contagem_nomes.items():
                print(f"{nome}: {frequencia}")

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

    # Função para tratar os dados de todos os PDFs
    def tratarTodosOsPdfs(self):
        textosExtraidos = self.lerTodosArquivos()  # Lê o conteúdo de todos os PDFs
        resultados = {}  # Para armazenar os resultados por arquivo

        for nomeArquivo, texto in textosExtraidos.items():
            print(f"\nProcessando dados do arquivo: {nomeArquivo}")
            
            # Extrair códigos de cliente do texto
            codigosClientes = self.pegarCodigoClientes(texto)
            clientes = [
                (codigo, self.nomeClienteComCodigo(int(codigo)))
                for codigo in codigosClientes
            ]

            # Contar os tipos de serviço
            tipos_servico = self.contarTiposServico(texto)

            # Salvar resultados
            resultados[nomeArquivo] = {
                "clientes": clientes,
                "tipos_servico": tipos_servico
            }

        return resultados

    # Exibe os dados tratados de todos os PDFs
    def mostrarDadosTratadosDeTodos(self):
        resultados = self.tratarTodosOsPdfs()
        frequencias_nomes = self.listarFrequenciaNomesPorArquivo()  # Frequências de nomes por arquivo

        for nomeArquivo, dados in resultados.items():
            print(f"\nResultados para o arquivo {nomeArquivo}:")
            
            print("\nCódigos de clientes e nomes correspondentes:")
            for codigo, nomeCliente in dados["clientes"]:
                print(f"Código {codigo}: {nomeCliente}")
            
            print("\nContagem de tipos de serviço:")
            for tipo, contagem in dados["tipos_servico"].items():
                print(f"{tipo}: {contagem}")

              # Exibe a frequência de nomes dos desenvolvedores
            print("\nFrequência de nomes de desenvolvedores:")
            if nomeArquivo in frequencias_nomes:
                for nome, frequencia in frequencias_nomes[nomeArquivo].items():
                   print(f"{nome}: {frequencia}")
            else:
                print("Nenhum nome encontrado para este arquivo.")
        