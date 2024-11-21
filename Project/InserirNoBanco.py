import psycopg2
from TratarDados import TratarDados

class InserirNoBanco(TratarDados):
    def __init__(self, caminhoPasta, conexaoDB):
        super().__init__(caminhoPasta)
        self.conexaoDB = conexaoDB

    def salvarDadosNoBanco(self):
        try:
            cursor = self.conexaoDB.cursor()

            # Dados tratados
            resultados = self.tratarTodosOsPdfs()
            frequencias_nomes = self.listarFrequenciaNomesPorArquivo()

            for nomeArquivo, dados in resultados.items():
                # Inserir dados de clientes
                for codigo, nomeCliente in dados["clientes"]:
                    cursor.execute("""
                        INSERT INTO clientes (codigocliente, nomecliente, nomearquivo)
                        VALUES (%s, %s, %s)
                    """, (codigo, nomeCliente, nomeArquivo))

                # Inserir dados de tipos de serviço
                for tipo, contagem in dados["tipos_servico"].items():
                    cursor.execute("""
                        INSERT INTO tiposervico (tiposervico, quantidadeservico, nomeArquivo)
                        VALUES (%s, %s, %s)
                    """, (tipo, contagem, nomeArquivo))

                # Inserir frequência de desenvolvedores
                if nomeArquivo in frequencias_nomes:
                    for nome, frequencia in frequencias_nomes[nomeArquivo].items():
                        cursor.execute("""
                            INSERT INTO desenv (desenvolvedores, frequenciadesenv, nomearquivo)
                            VALUES (%s, %s, %s)
                        """, (nome, frequencia, nomeArquivo))

            # Confirmação das transações
            self.conexaoDB.commit()
            print("Dados inseridos no banco com sucesso!")

        except psycopg2.Error as e:
            print(f"Erro ao inserir dados no banco: {e}")
            self.conexaoDB.rollback()

        finally:
            cursor.close()

conexaoDB = psycopg2.connect(
            database='DBDados',
            host='localhost',
            user='postgres',
            password='lucas2908',
            port='5432'
        )


# Criar instância do tratador de dados com banco
tratar_dados = InserirNoBanco("C:/Users/Lucas Hack/Desktop/trabalho de ciência de dados/PDFs", conexaoDB)

# Salvar os dados tratados no banco
tratar_dados.salvarDadosNoBanco()

