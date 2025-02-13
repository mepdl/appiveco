import PyPDF2
from openpyxl import Workbook

def pdf_para_excel(caminho_pdf, caminho_excel):
    """
    Lê informações de um arquivo PDF e as grava em uma planilha Excel.

    Args:
        caminho_pdf (str): O caminho para o arquivo PDF.
        caminho_excel (str): O caminho para o arquivo Excel de saída.
    """

    try:
        with open(caminho_pdf, "rb") as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            numero_paginas = len(leitor_pdf.pages)

            workbook = Workbook()
            planilha = workbook.active

            # Escreva o cabeçalho da planilha (se necessário)
            # planilha.append(["Coluna 1", "Coluna 2", ...])

            for pagina in range(numero_paginas):
                pagina_atual = leitor_pdf.pages[pagina]
                texto = pagina_atual.extract_text()

                # Extraia as informações do texto do PDF
                # Isso dependerá do formato do seu PDF.
                # Você pode usar expressões regulares ou outras técnicas.
                # Exemplo (adaptar ao seu caso):
                for linha in texto.splitlines():
                    # Separe os dados por vírgula, espaço, etc.
                    dados = linha.split(",")
                    planilha.append(dados)

            workbook.save(caminho_excel)
            print(f"Arquivo Excel '{caminho_excel}' criado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: Arquivo PDF '{caminho_pdf}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar PDF: {e}")

# Exemplo de uso
pdf_para_excel("./ESTOQUE VG 12-02-2025.pdf", "./arquivo_excel.xlsx")