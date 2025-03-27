# Análise de Dados de Operadoras de Saúde

Este projeto tem como objetivo estruturar e analisar os dados financeiros de operadoras de planos de saúde utilizando um banco de dados. Os dados foram obtidos a partir de dois repositórios públicos fornecidos pela ANS, tratados, importados para um banco de dados PostgreSQL e, em seguida, foram feitas análises para responder a perguntas específicas sobre as operadoras.

## Descrição

O projeto consiste nas seguintes etapas principais:

1. **Coleta de Dados**: Os dados foram baixados diretamente dos repositórios públicos da ANS:
    - **Demonstrações Contábeis**: Disponíveis [aqui](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/).
    - **Dados Cadastrais das Operadoras Ativas**: Disponíveis [aqui](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/).

2. **Tratamento dos Dados**: O arquivo CSV obtido da ANS estava com valores numéricos no formato brasileiro (vírgula como separador decimal). Para corrigir esse problema, foi utilizado um script PowerShell para substituir a vírgula por ponto, tornando os números compatíveis com o formato esperado pelo banco de dados:

    ```powershell
    (Get-Content -Path "C:\Temp\4T2024.csv" -Encoding UTF8) | 
    ForEach-Object { [System.Text.Encoding]::ASCII.GetString([System.Text.Encoding]::UTF8.GetBytes($_)) -replace '(\d),(\d)', '$1.$2'} | 
    Set-Content -Path "C:\Temp\4T2024_clean.csv" -Encoding UTF8
    ```

3. **Importação dos Dados para o Banco de Dados**: Após o tratamento, os dados foram importados para o banco de dados PostgreSQL utilizando o comando `\copy`:

    ```sql
    \copy demonstracoes_contabeis FROM 'C:\Temp\4T2024_clean.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
    ```

4. **Estruturação e Criação de Tabelas**: As tabelas necessárias foram criadas no banco de dados utilizando scripts SQL, levando em consideração o formato dos dados e a estrutura necessária para armazenar as informações de forma eficiente, estão presentes no arquivo scripts.

5. **Consultas Analíticas**: Foram elaboradas queries analíticas para responder às seguintes perguntas:
    - Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR" no último trimestre?
    - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

## Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o PostgreSQL instalado e configurado em sua máquina. Além disso, você precisará dos seguintes arquivos:
- O arquivo CSV com os dados tratáveis.
- O arquivo SQL contendo as queries para criação das tabelas e as queries analíticas.

### 2. Importando os Dados

Depois de corrigir o arquivo CSV, siga as instruções abaixo para importar os dados para o banco de dados PostgreSQL:

1. Abra o terminal do PostgreSQL e conecte-se ao seu banco de dados.
2. Execute o comando `\copy` para importar os dados:

    ```sql
    \copy demonstracoes_contabeis FROM 'C:\Temp\4T2024_clean.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8'
    ```

### 3. Criando as Tabelas

Use o arquivo SQL para criar as tabelas necessárias para armazenar os dados. Isso pode ser feito com o seguinte comando SQL:

```sql
-- Criação das tabelas (incluir código completo de criação aqui)
