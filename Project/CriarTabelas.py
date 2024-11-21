import psycopg2
from InserirNoBanco import InserirNoBanco

conexaoDB = psycopg2.connect(database = 'DBDados',
                             host='localhost',
                             user='postgres',
                             password='lucas2908',
                             port='5432',)

# caso a resposta for 1 a conexão deu certo
print(f'Resposta: {conexaoDB.status}')

cursor = conexaoDB.cursor()

cursor.execute("""

    CREATE TABLE clientes (
        nomeArquivo VARCHAR(50),
        codigoCliente INTEGER,
        nomeCliente VARCHAR(50),
    );
    """)

cursor.execute("""

    CREATE TABLE tipoServico (
        nomeArquivo VARCHAR(50),
        tipoServico VARCHAR(50),
        quantidadeServico INTEGER,
    );
    """)

cursor.execute("""

    CREATE TABLE desenv (
        nomeArquivo VARCHAR(50),
        desenvolvedores VARCHAR(50),
        frequenciaDesenv INTEGER
    );
    """)
       
# Confirmando as alterações no banco de dados
conexaoDB.commit()


print("Tabelas criada com sucesso!")

cursor.close()
conexaoDB.close()