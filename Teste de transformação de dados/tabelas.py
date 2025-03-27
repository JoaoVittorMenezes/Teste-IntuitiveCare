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
    # Pegando o cabeçalho da primeira tabela
    first_table = tables[0].df
    headers = first_table.iloc[0].tolist()  # Captura os nomes das colunas
    num_cols = len(headers)  # Número esperado de colunas
    print(f"Cabeçalhos detectados: {headers}")

    # Criando lista para armazenar tabelas válidas
    dfs = []

    for i, table in enumerate(tables):
        df = table.df

        # Verifica se o número de colunas bate com o esperado
        if df.shape[1] == num_cols:
            df.columns = headers  # Aplica cabeçalhos
            df = df.iloc[1:]  # Remove a primeira linha (cabeçalho repetido)
            dfs.append(df)
        else:
            print(f"❌ Tabela na página {i+3} ignorada (colunas incompatíveis)")

    # Concatenar tabelas válidas
    if dfs:
        df_final = pd.concat(dfs, ignore_index=True)

        # Limpeza de dados
        df_final = df_final.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        # Substituir abreviações de OD e AMB conforme legenda do rodapé
        legenda = {
            "OD": "Procedimentos Odontológicos",
            "AMB": "Procedimentos Ambulatoriais"
        }
        df_final.rename(columns=legenda, inplace=True)

        # Nome do arquivo CSV
        csv_filename = "Teste_JoaoVittorMenezes.csv"

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

        print(f"✅ Arquivo {zip_output} gerado com sucesso!")
    else:
        print("⚠️ Nenhuma tabela válida foi extraída.")
else:
    print("⚠️ Nenhuma tabela encontrada. Tente ajustar os parâmetros.")
