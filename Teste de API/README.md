# Projeto de Busca de Operadoras de Saúde

Este projeto consiste na criação de uma API com o framework FastAPI para realizar a busca de operadoras de saúde e uma interface web utilizando Vue.js para interagir com a API. O objetivo é permitir a busca textual em uma lista de operadoras e exibir os resultados de forma dinâmica.

## Descrição do Projeto

O projeto foi dividido nas seguintes etapas:

1. **Criação da API**:
    - Foi desenvolvido um servidor utilizando o **FastAPI** em Python.
    - A API oferece uma rota que permite buscar operadoras com base em um texto, retornando os registros mais relevantes da base de dados.

2. **Desenvolvimento da Interface Web**:
    - A interface foi desenvolvida utilizando o **Vue.js**.
    - Ela interage com a API por meio de requisições **GET**, permitindo que os usuários busquem operadoras de saúde através de uma caixa de pesquisa.

3. **Carregamento dos Dados**:
    - Os dados das operadoras de saúde foram obtidos a partir de um arquivo CSV com as informações das operadoras ativas na ANS (Agência Nacional de Saúde Suplementar).
    - A base de dados foi carregada em memória no servidor para realizar as buscas de maneira eficiente.

## Como Funciona

A interface web permite que o usuário digite o nome de uma operadora, e a API realiza uma busca no CSV de dados, retornando as operadoras que correspondem ao termo de pesquisa. O resultado é mostrado na interface em uma tabela, com informações como Razão Social, CNPJ, Registro ANS e Modalidade.

## Funcionalidades

- **Busca de Operadoras**: O usuário pode digitar o nome da operadora para encontrar registros correspondentes.
- **Exibição de Resultados**: Os resultados da busca são exibidos em formato tabular, com as principais informações das operadoras.
- **Exibição de Mensagens de Erro**: Caso não haja resultados ou ocorra algum erro, mensagens apropriadas são exibidas.

## Como Executar o Projeto

### 1. Pré-requisitos

- **Python**: Certifique-se de que o Python esteja instalado em sua máquina. Recomenda-se usar uma versão >= 3.8.
- **Vue.js**: O frontend foi desenvolvido utilizando Vue.js. Você precisará do **Node.js** e do **Vue CLI** instalados.

Para instalar o Node.js, você pode fazer o download a partir do [site oficial](https://nodejs.org/). Certifique-se de instalar a versão LTS (Long Term Support).

### 2. Configuração do Backend (API)

1. Crie um ambiente virtual em Python e instale as dependências necessárias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    pip install fastapi pandas uvicorn
    ```

2. Salve o código da API em um arquivo, por exemplo, `server.py`, e execute o servidor:

    ```bash
    uvicorn server:app --reload
    ```

    O servidor estará disponível em `http://localhost:8000`.

### 3. Configuração do Frontend (Vue.js)

1. **Instalar o Node.js**:
    - Certifique-se de que o **Node.js** esteja instalado. Caso contrário, faça o download do instalador no [site oficial do Node.js](https://nodejs.org/).

2. Crie um novo projeto Vue.js ou utilize o código fornecido. Se precisar criar um novo projeto, use o Vue CLI:

    ```bash
    vue create nome-do-projeto
    ```

3. Instale a biblioteca `axios` para realizar requisições HTTP:

    ```bash
    npm install axios
    ```

4. Adicione o código do frontend (`App.vue`) ao seu projeto.

5. Para rodar a aplicação, execute:

    ```bash
    npm run serve
    ```

    A interface estará disponível em `http://localhost:8080`.

### 4. Testando a Busca

Após configurar e rodar o backend e o frontend, abra o navegador e acesse a interface em `http://localhost:8080`. Na caixa de pesquisa, digite o nome de uma operadora e veja os resultados sendo retornados pela API.

## Estrutura do Repositório

O repositório contém os seguintes arquivos:

- `server.py`: Código da API FastAPI que manipula a busca de operadoras.
- `App.vue`: Código do frontend em Vue.js para a interface de busca.
- `README.md`: Este arquivo com todas as instruções e explicações do projeto.

## Como Usar a API

A API possui uma rota para realizar a busca de operadoras:

- **GET `/buscar`**: Realiza uma busca por nome da operadora e retorna os registros correspondentes.

### Parâmetros da Rota

- `query`: O termo de busca que será comparado com a "Razão Social" das operadoras (case-insensitive).

Exemplo de requisição GET:

```bash
http://localhost:8000/buscar?query=Unimed
