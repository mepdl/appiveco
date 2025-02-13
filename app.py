import streamlit as st
import pandas as pd

# Carregamento dos dados
try:
    mtz_data = pd.read_excel("./ESTOQUE VG 12-02-2025.xlsx")
    # ... (carregue os outros arquivos Excel)
except FileNotFoundError:
    st.error("Erro: Arquivo Excel não encontrado. Verifique o caminho.")
    st.stop()

# Conversão da coluna "ANO" para datetime year
try:
    mtz_data["ANO"] = pd.to_datetime(mtz_data["ANO"], format="%Y").dt.year
    # ... (faça o mesmo para os outros DataFrames)
except ValueError:
    st.error("Erro: A coluna 'ANO' contém valores inválidos. Verifique o formato.")

# Conversão da coluna "MODELO" para datetime year (se aplicável)
# Se a coluna "MODELO" contiver o ano, você pode usar uma função para extraí-lo
# Exemplo:
def extrair_ano_modelo(modelo):
    # Use expressões regulares para encontrar o ano no modelo
    # ...
    return ano

# mtz_data["MODELO_ANO"] = mtz_data["MODELO"].apply(extrair_ano_modelo)
# mtz_data["MODELO_ANO"] = pd.to_datetime(mtz_data["MODELO_ANO"], format="%Y").dt.year
# ... (faça o mesmo para os outros DataFrames)

# Título da aplicação
st.title("Aplicação de Dados de Veículos")

# Menu de seleção
opcao = st.selectbox("Selecione uma opção:", ["MTZ", "ROO", "SNP", "CG"])

# Exibição da tabela (com filtro por ano)
if opcao == "MTZ":
    st.write(mtz_data)
elif opcao == "ROO":
    st.write(roo_data)
elif opcao == "SNP":
    st.write(snp_data)
elif opcao == "CG":
    st.write(cg_data)
