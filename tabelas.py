import pdfplumber
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

pdf_path = "tables\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

def extract_table(page_num):
    with pdfplumber.open(pdf_path) as pdf:
        table = pdf.pages[page_num].extract_table()
        return pd.DataFrame(table[1:], columns=table[0]) if table else None

with pdfplumber.open(pdf_path) as pdf:
    num_pages = len(pdf.pages)

with ThreadPoolExecutor() as executor:
    tables = list(executor.map(extract_table, range(num_pages)))

df_final = pd.concat([df for df in tables if df is not None], ignore_index=True)

df_final.to_csv("tabelas_extraidas.csv", index=False)


print(df_final)



chrome_driver_path = r'C:\\Users\\joaov\\OneDrive\\Área de Trabalho\\chromedriver-win64\\chromedriver.exe' # Atualize para o caminho correto
