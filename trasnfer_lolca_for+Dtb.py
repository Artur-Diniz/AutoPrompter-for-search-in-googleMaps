import pandas as pd
from Crud.Localcrud import LocalCRUD

    
# Caminho da planilha
arquivo = "categoria+cidades.xlsx"

# Ler a planilha (ajuste o nome da aba se necessário)
df = pd.read_excel(arquivo)

# Normalizar os nomes das colunas (caso tenha espaços)
df.columns = df.columns.str.strip()

# Iterar por cada linha e criar as categorias
for _, linha in df.iterrows():
    Cidade = str(linha["Cidade"]).strip()
    bairro = str(linha["Bairro"]).strip()
    if bairro=='nan':
        bairro=''
    print("Cidade: "+Cidade+" || Bairro: "+bairro)
    LocalCRUD.criar(Cidade, bairro)