import pandas as pd
from Crud.Categoriacrud import CategoriaCRUD

    
# Caminho da planilha
arquivo = "categoria+cidades.xlsx"

# Ler a planilha (ajuste o nome da aba se necessário)
df = pd.read_excel(arquivo)

# Normalizar os nomes das colunas (caso tenha espaços)
df.columns = df.columns.str.strip()

# Iterar por cada linha e criar as categorias
for _, linha in df.iterrows():
    prioridade = int(linha["Prioridade"])
    categoria = str(linha["Categoria de Empreendimento"]).strip()
    # print("Categoria: "+categoria+f"|| Prioridade: {prioridade}")
    CategoriaCRUD.criar(categoria, prioridade)