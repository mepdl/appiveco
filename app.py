import streamlit as st
import pandas as pd

# Carregamento dos dados dos arquivos Excel
try:
    mtz_data = pd.read_excel(".ESTOQUE VG 12-02-2025.xlsx")
    roo_data = pd.read_excel("./ESTOQUE VG 12-02-2025.xlsx")  # Substitua pelo arquivo correto
    snp_data = pd.read_excel("./ESTOQUE VG 12-02-2025.xlsx")  # Substitua pelo arquivo correto
    cg_data = pd.read_excel("./ESTOQUE VG 12-02-2025.xlsx")  # Substitua pelo arquivo correto
except FileNotFoundError:
    st.error("Erro: Arquivo Excel não encontrado. Verifique o caminho.")
    st.stop()  # Para a execução do aplicativo

# Título da aplicação
st.title("Aplicação de Dados de Veículos")

# Menu de seleção
opcao = st.selectbox("Selecione uma opção:", ["MTZ", "ROO", "SNP", "CG"])

# Função para exibir a tabela com filtro por ano
def exibir_tabela(data):
    try:
        ano = st.number_input("Digite o ano para filtrar:", min_value=2000, max_value=2024, value=2024)
        tabela_filtrada = data[data["ANO"] == ano]
        st.dataframe(tabela_filtrada)
    except KeyError:
        st.error("Erro: Coluna 'ANO' não encontrada no arquivo Excel.")
    except TypeError:
        st.error("Erro: Verifique se a coluna 'ANO' está formatada como número.")

# Exibição da tabela de acordo com a opção selecionada
if opcao == "MTZ":
    exibir_tabela(mtz_data)
elif opcao == "ROO":
    exibir_tabela(roo_data)
elif opcao == "SNP":
    exibir_tabela(snp_data)
elif opcao == "CG":
    exibir_tabela(cg_data)
