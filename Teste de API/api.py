from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import math

app = FastAPI()

# Permitir CORS para o Vue.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # URL do seu front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar o CSV em memória (substitua 'operadoras.csv' pelo nome correto)
df = pd.read_csv(r"C:\Users\joaov\OneDrive\Área de Trabalho\Teste IntuitiveCare\Teste de API\Relatorio_cadop.csv", delimiter=";", encoding="utf-8")


def corrigir_valores_invalidos(dado):
    """Substitui valores inválidos (NaN e infinitos) por None"""
    if isinstance(dado, float) and (math.isnan(dado) or math.isinf(dado)):
        return None  # Ou outro valor padrão, como 0
    elif isinstance(dado, dict):
        return {k: corrigir_valores_invalidos(v) for k, v in dado.items()}
    elif isinstance(dado, list):
        return [corrigir_valores_invalidos(v) for v in dado]
    return dado


@app.get("/buscar")
def buscar_operadora(query: str = Query(..., description="Nome da operadora")):
    # Filtrar as operadoras que contenham o texto na busca (ignorando maiúsculas e minúsculas)
    resultados = df[df["Razao_Social"].str.contains(query, case=False, na=False)]
    
    # Corrigir valores inválidos antes de retornar
    return corrigir_valores_invalidos(resultados.to_dict(orient="records"))

# Rodar o servidor com: uvicorn server:app --reload
