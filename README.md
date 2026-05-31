# Bancos de Dados 2 - Preparacao de Dados para Machine Learning

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Repositorio utilizado na disciplina de Bancos de Dados 2 do curso Tecnico EAD em Informatica para Internet do IFCE Campus Maranguape, com foco em extracao, limpeza e preparacao de dados para tarefas de Machine Learning.

## Visao Geral

Este projeto foi organizado para praticar um fluxo comum em projetos de dados:

1. Ler dados de fontes estruturadas (SQL).
2. Gerar e diagnosticar dados com problemas reais (nulos, outliers, duplicatas e inconsistencias).
3. Preparar dados para etapas posteriores de analise e modelagem.

## Estrutura do Repositorio

```text
.
|- main.py
|- dirty_iris.py
|- requirements.txt
|- data/
|  |- README.md
|- LICENSE
|- README.md
```

## Arquivos Principais

- `dirty_iris.py`: gera uma versao "suja" do dataset Iris para treino de limpeza e qualidade de dados.
- `main.py`: exemplo de consulta SQL com `sqlite3` + `pandas` para o dataset Iris.
- `requirements.txt`: dependencias do projeto.

## Requisitos

- Python 3.10 ou superior
- `pip` atualizado

## Instalacao

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Base de Dados (Obrigatorio)

Este projeto nao baixa bancos automaticamente.

Clone o repositorio de bancos dentro da pasta `data`:

```bash
mkdir -p data
git clone https://github.com/davidjamesknight/SQLite_databases_for_learning_data_science.git data/SQLite_databases_for_learning_data_science
```

Depois disso, o arquivo do Iris deve estar em:

`data/SQLite_databases_for_learning_data_science/iris.db`

## Como Executar

### 1) Gerar e diagnosticar um Iris com problemas

```bash
python dirty_iris.py
```

Esse script imprime no terminal:

- tamanho do dataset apos insercao de duplicatas
- total de valores ausentes por coluna
- contagem de outliers por atributo numerico
- inconsistencias em nomes de especies
- quantidade de linhas duplicadas

### 2) Executar consulta SQL do Iris

O exemplo em `main.py` depende de um banco SQLite local do Iris.

Use o arquivo clonado em `data/SQLite_databases_for_learning_data_science/iris.db` e execute:

```bash
python main.py
```

## Objetivos de Aprendizagem

- Extrair dados de bancos relacionais usando SQL e Pandas.
- Tratar dados incompletos e inconsistentes.
- Identificar e lidar com outliers e duplicatas.
- Preparar datasets para etapas de modelagem.

## Dependencias

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

Observacao: `sqlite3` faz parte da biblioteca padrao do Python e normalmente nao precisa ser instalado via `pip`.

## Licenca

Este projeto esta licenciado sob a licenca MIT. Consulte o arquivo [LICENSE](LICENSE).
