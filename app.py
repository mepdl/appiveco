import streamlit as st
import pandas as pd
import os

# Diretório onde os arquivos XLSX estão armazenados
XLSX_DIR = "xlsx/lojas"
LOJAS = ["MTZ", "ROO", "SNP", "CG"]

# Função para listar arquivos XLSX disponíveis em uma unidade específica
def list_xlsx(directory):
    return [f for f in os.listdir(directory) if f.endswith(".xlsx")]

# Função para ler dados do arquivo XLSX
def read_xlsx(file_path):
    # Lê o arquivo Excel
    df = pd.read_excel(file_path)
    
    # Excluir a coluna que vem antes da coluna "COD. CRM"
    if "COD. CRM" in df.columns:
        cod_crm_index = df.columns.get_loc("COD. CRM")
        if cod_crm_index > 0:  # Se houver uma coluna antes de "COD. CRM"
            df = df.drop(df.columns[cod_crm_index - 1], axis=1)  # Remove a coluna anterior
    
    # Definir colunas desejadas
    colunas_desejadas = ["COD. CRM", "MODELO", "CHASSI", "ANO", "COR", "MARCA PNEU", "DIAS ESTOQUE"]
    
    # Filtrar apenas as colunas desejadas
    df = df[[col for col in colunas_desejadas if col in df.columns]]
    
    # Converter a coluna "COD. CRM" para inteiro, removendo vírgulas
    if "COD. CRM" in df.columns:
        df["COD. CRM"] = df["COD. CRM"].astype(str).str.replace(",", "").astype(int)
    
    return df

# Interface do aplicativo
st.title("Consulta de Veículos IVECO")

# Selecionar unidade (loja)
unidade = st.selectbox("Selecione a Unidade:", LOJAS)

# Listar arquivos na unidade selecionada
pdf_dir = os.path.join(XLSX_DIR, unidade)
pdfs = list_xlsx(pdf_dir)

if pdfs:
    selected_pdf = pdfs[0]  # Pega automaticamente o primeiro arquivo disponível
    pdf_path = os.path.join(pdf_dir, selected_pdf)
    df = read_xlsx(pdf_path)
    
    if df.empty:
        st.write("Erro: Não foi possível ler dados válidos do arquivo XLSX.")
    else:
        st.write("### Dados extraídos:")
        st.dataframe(df)
else:
    st.write(f"Nenhum arquivo XLSX encontrado para a unidade {unidade}.")