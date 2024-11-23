import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas as pd

# Configuração da conexão ao banco de dados
engine = create_engine('postgresql+psycopg2://postgres:lucas2908@localhost:5432/DBDados')

# Carregar os dados das tabelas em DataFrames
df_clientes = pd.read_sql("SELECT * FROM clientes", engine)
df_desenv = pd.read_sql("SELECT * FROM desenv", engine)
df_tiposervico = pd.read_sql("SELECT * FROM tiposervico", engine)

# Fazer merge das tabelas com base na coluna 'nomearquivo'
df_merged = df_clientes.merge(df_desenv, on="nomearquivo").merge(df_tiposervico, on="nomearquivo")

# Agregar dados por tipo de serviço
df_servicos = df_merged.groupby("tiposervico")["quantidadeservico"].sum().reset_index()

# Configurar tema escuro e paletas ajustadas
sns.set_theme(style="darkgrid")
plt.style.use("dark_background")
custom_palette = sns.color_palette("Set2")

# Gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(df_servicos["quantidadeservico"], labels=df_servicos["tiposervico"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(df_servicos)))
plt.title("Proporção dos Tipos de Serviço")
plt.show()


# Gráfico de barras ajustado
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df_merged,
    x="nomecliente",
    y="frequenciadesenv",
    hue="desenvolvedores",
    palette="colorblind"  
)
plt.xticks(rotation=45, color="white")
plt.yticks(color="white")
plt.title("Frequência de Desenvolvedores por Cliente", color="white")
plt.xlabel("Cliente", color="white")
plt.ylabel("Frequência", color="white")
plt.legend(title="Desenvolvedores", labelcolor="white", facecolor="black")
plt.tight_layout()
plt.show()





# Contagem de tipos de serviço por cliente
plt.figure(figsize=(12, 8))
sns.countplot(
    data=df_merged,
    x="nomecliente",
    hue="tiposervico",
    palette="Set2"
)

# Ajustes no gráfico
plt.title("Contagem de Tipos de Serviço por Cliente", color="white")
plt.xlabel("Cliente", color="white")
plt.ylabel("Contagem de Tipos de Serviço", color="white")
plt.xticks(rotation=45, color="white")
plt.yticks(color="white")
plt.legend(title="Tipo de Serviço", labelcolor="white", facecolor="black")
plt.tight_layout()

# Exibir gráfico
plt.show()


