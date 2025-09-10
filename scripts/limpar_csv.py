import pandas as pd

# Caminhos
input_csv = "data-raw/splor_202506_servidores.csv"
output_csv = "data-raw/splor_202506_servidores_clean.csv"  # pode substituir o original se quiser

# Ler CSV com delimitador ; e encoding utf-8-sig
df = pd.read_csv(input_csv, delimiter=";", encoding="utf-8-sig")

# Remover linhas completamente vazias
df.dropna(how="all", inplace=True)

# Normalizar nomes das colunas
rename_columns = {
    "Ano/Mês Referência": "ano_mes_referencia",
    "MASP": "masp",
    "Nº Admissão": "num_admissao",
    "Masp/Admissão": "masp_admissao",
    "Nome Servidor": "nome_servidor",
    "CPF": "cpf",
    "Data Completa": "data_completa",
    "E-mail": "email",
    "Cod Sit Funcional": "cod_sit_funcional",
    "Situação Funcional": "situacao_funcional",
    "Cod Sit Servidor": "cod_sit_servidor",
    "Situação Servidor": "situacao_servidor",
    "Carreira Efetiva.Cod Carreira": "carreira_efetiva_cod_carreira",
    "Cod Carreira.Carreira": "cod_carreira_carreira",
    "Nivel": "nivel",
    "Carreira Efetiva.Grau": "carreira_efetiva_grau",
    "Cargo Comissão.Carreira": "cargo_comissao_carreira",
    "Carreira.Cod Carreira": "carreira_cod_carreira",
    "Cod Cargo Comissão": "cod_cargo_comissao",
    "Cargo Comissão": "cargo_comissao",
    "Cargo Comissão.Nível": "cargo_comissao_nivel",
    "Nº Vaga": "num_vaga",
    "Data Exercício": "data_exercicio",
    "Cod Função Gratificada": "cod_funcao_gratificada",
    "Função Gratificada": "funcao_gratificada",
    "Função Gratificada.Nível": "funcao_gratificada_nivel",
    "Função Gratificada.Grau": "funcao_gratificada_grau",
    "Data Início": "data_inicio",
    "Cod Orçamento Lotação": "cod_orcamento_lotacao",
    "Instituição Lotação": "instituicao_lotacao",
    "Sigla": "sigla",
    "Cod Unidade Lotação": "cod_unidade_lotacao",
    "Unidade Lotação": "unidade_lotacao",
    "Cod Orçamento Exercício": "cod_orcamento_exercicio",
    "Instituição Exercício": "instituicao_exercicio",
    "Cod Unidade Exercício": "cod_unidade_exercicio",
    "Unidade Exercício": "unidade_exercicio"
}

df.rename(columns=rename_columns, inplace=True)

# Ajustar tipos de dados
# CPF como string para manter zeros à esquerda
df["cpf"] = df["cpf"].astype(str)

# Datas como datetime
for col in ["data_completa", "data_exercicio", "data_inicio"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

# Campos numéricos inteiros
int_columns = [
    "num_admissao", "masp_admissao", "cod_sit_funcional", "cod_sit_servidor",
    "carreira_cod_carreira", "num_vaga", "cod_orcamento_lotacao",
    "cod_unidade_lotacao", "cod_orcamento_exercicio", "cod_unidade_exercicio"
]

for col in int_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")  # permite NA

# Salvar CSV limpo
df.to_csv(output_csv, index=False, sep=";", encoding="utf-8-sig")

print(f"CSV processado e salvo em: {output_csv}")


