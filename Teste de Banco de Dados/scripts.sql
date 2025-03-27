CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(100) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_comercializacao VARCHAR(20),
    data_registro_ans DATE
);


CREATE TABLE demonstracoes_contabeis (
    data DATE NOT NULL,
    registro_ans VARCHAR(20) NOT NULL,
    codigo_conta VARCHAR(20) NOT NULL,
    descricao text NOT NULL,
    valor_saldo_inicial DECIMAL(15, 2) NOT NULL,
    valor_saldo_final DECIMAL(15, 2) NOT NULL,
);

# Query da primeira pergunta:

SELECT 
    o.razao_social,
    o.nome_fantasia,
    SUM(d.valor_saldo_final - d.valor_saldo_inicial) AS despesas_trimestre
FROM 
    demonstracoes_contabeis d
LEFT JOIN 
    operadoras o ON d.registro_ans = o.registro_ans
WHERE 
    d.descricao LIKE '%MEDICO HOSPITALAR%'
    AND d.data = '01/10/2024'
GROUP BY 
    o.razao_social, o.nome_fantasia
ORDER BY 
    despesas_trimestre DESC
LIMIT 10;


#Query da segunda pergunta

SELECT 
    o.razao_social,
    o.nome_fantasia,
    SUM(d.valor_saldo_final - d.valor_saldo_inicial) AS despesas_ano
FROM 
    demonstracoes_contabeis d
LEFT JOIN 
    operadoras o ON d.registro_ans = o.registro_ans
WHERE 
    d.descricao LIKE '%EVENTOS%%MEDICO HOSPITALAR%'
    AND d.data >= '01/10/2024'
GROUP BY 
    o.razao_social, o.nome_fantasia
ORDER BY 
    despesas_ano DESC
LIMIT 10;