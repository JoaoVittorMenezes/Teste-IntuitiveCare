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

# Extração das tabelas do PDF
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
    df_final = pd.concat([table.df for table in tables], ignore_index=True)
    
    # Ajustando cabeçalhos
    df_final.columns = df_final.iloc[0]
    df_final = df_final.drop(0).reset_index(drop=True)
    
    # Limpeza de dados
    df_final = df_final.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Substituir abreviações de OD e AMB conforme legenda do rodapé
    legenda = {
        "OD": "Procedimentos Odontológicos",
        "AMB": "Procedimentos Ambulatoriais"
    }
    df_final.rename(columns=legenda, inplace=True)

    # Nome do arquivo CSV
    csv_filename = "Teste_SeuNome.csv"

    # Salvando CSV
    df_final.to_csv(
        csv_filename,
        index=False,
        sep=";",  # Ponto e vírgula como separador
        quoting=csv.QUOTE_MINIMAL,
        encoding="utf-8-sig"
    )

    # Compactando o CSV em um ZIP
    zip_output = f"Teste_SeuNome.zip"
    with zipfile.ZipFile(zip_output, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(csv_filename)

    print(f"Arquivo {zip_output} gerado com sucesso!")
else:
    print("Nenhuma tabela encontrada. Tente ajustar os parâmetros.")
