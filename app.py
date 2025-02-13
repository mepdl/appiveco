import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Carregamento dos dados dos arquivos Excel
mtz_data = pd.read_excel("ESTOQUE VG.xlsx")
roo_data = pd.read_excel("ESTOQUE ROO.xlsx")
snp_data = pd.read_excel("ESTOQUE ROO.xlsx")
cg_data = pd.read_excel("ESTOQUE VG.xlsx")

# Título da aplicação
st.title("Aplicação de Dados de Veículos")

# Menu de seleção
opcao = st.selectbox("Selecione uma opção:", ["MTZ", "ROO", "SNP", "CG"])

# Função para exibir a tabela com filtros e gráfico de pizza
def exibir_tabela(data):
    # Cálculo das quantidades e porcentagens por segmento
    contagem_segmentos = data["SEGMENTO"].value_counts()
    porcentagem_segmentos = contagem_segmentos / contagem_segmentos.sum() * 100

    # Criação do gráfico de pizza com título
    fig = go.Figure(data=[go.Pie(labels=contagem_segmentos.index, 
                                 values=contagem_segmentos.values,
                                 hoverinfo='label+percent', 
                                 textinfo='value')],
                     layout=go.Layout(title="Distribuição de Veículos por Segmento"))  # Adiciona o título aqui

    st.plotly_chart(fig)  # Exibe o gráfico de pizza primeiro

    # Filtro por STATUS
    status = st.multiselect("Selecione o(s) STATUS para filtrar:", data["STATUS"].unique())
    if status:
        tabela_filtrada = data[data["STATUS"].isin(status)]
    else:
        tabela_filtrada = data.copy()  # Exibe todos os dados se nenhum status for selecionado

    # Filtro por SEGMENTO
    segmento = st.multiselect("Selecione o(s) SEGMENTO(s) para filtrar:", data["SEGMENTO"].unique())
    if segmento:
        tabela_filtrada = tabela_filtrada[tabela_filtrada["SEGMENTO"].isin(segmento)]

    st.data_editor(tabela_filtrada, height=400)  # Tabela interativa com quebra de texto automática

# Exibição da tabela de acordo com a opção selecionada
if opcao == "MTZ":
    exibir_tabela(mtz_data)
elif opcao == "ROO":
    exibir_tabela(roo_data)
elif opcao == "SNP":
    exibir_tabela(snp_data)
elif opcao == "CG":
    exibir_tabela(cg_data)