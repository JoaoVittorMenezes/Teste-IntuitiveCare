import zipfile
import io
import camelot
import pandas as pd
import csv

# Caminho do ZIP e nome do PDF dentro dele
zip_path = "Anexos.zip"
pdf_name = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Extraindo o PDF do ZIP para a memória
with zipfile.ZipFile(zip_path, "r") as z:
    with z.open(pdf_name) as pdf_file:
        pdf_bytes = io.BytesIO(pdf_file.read())

# Usando Camelot para ler o PDF extraído da memória
tables = camelot.read_pdf(
    pdf_bytes,
    pages="3-181",
    flavor="stream",
    strip_text='\n',
    edge_tol=600,
    row_tol=15,
    column_tol=15
)

print(f"Tabelas extraídas: {len(tables)}")

if len(tables) > 0:
    # Concatenando todas as tabelas extraídas em um único DataFrame
    df_final = pd.concat([table.df for table in tables], ignore_index=True)
    
    # Tratamento do cabeçalho
    df_final.columns = df_final.iloc[0]
    df_final = df_final.drop(0).reset_index(drop=True)
    
    # Limpeza de dados (remoção de espaços extras)
    df_final = df_final.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Renomeando as colunas conforme o dicionário "legenda"
    legenda = {
            "OD": "Procedimentos Odontológicos",
            "AMB": "Procedimentos Ambulatoriais"
        }
    df_final.rename(columns=legenda, inplace=True)

    # Nome do arquivo CSV
    csv_filename = "Teste_JoaoVittorMenezes.csv"

    # Salvando o DataFrame como CSV
    df_final.to_csv(
        csv_filename,
        index=False,
        sep=";",  # Ponto e vírgula como separador
        quoting=csv.QUOTE_MINIMAL,
        encoding="utf-8-sig"
    )

    # Compactando o CSV em um novo arquivo ZIP
    zip_output = f"Teste_JoaoVittorMenezes.zip"
    with zipfile.ZipFile(zip_output, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(csv_filename)

    print("Arquivo gerado com sucesso!")
    print("\nPrimeiras linhas:")
    print(df_final.head())
else:
    print("Nenhuma tabela encontrada. Tente ajustar os parâmetros.")

print(f"Tabelas extraídas: {len(tables)}")
