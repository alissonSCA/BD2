import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

def criar_iris_sujo(nivel='medio', random_state=42):
    """
    Cria versão suja do dataset Iris
    
    Parâmetros:
    - nivel: 'leve', 'medio', 'pesado'
    - random_state: para reprodutibilidade
    """
    np.random.seed(random_state)
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species_name'] = iris.target_names[iris.target]
    
    if nivel == 'leve':
        # 2% de nulos, poucos outliers, 1% duplicatas
        df = _adicionar_nulos(df, 0.02)
        df = _adicionar_outliers_leves(df)
        df = _adicionar_duplicatas(df, 0.01)
        df = _inconsistencias_strings_leves(df)
        
    elif nivel == 'medio':
        # 5% de nulos, outliers moderados, 3% duplicatas
        df = _adicionar_nulos(df, 0.05)
        df = _adicionar_outliers_moderados(df)
        df = _adicionar_duplicatas(df, 0.03)
        df = _inconsistencias_strings_medias(df)
        
    elif nivel == 'pesado':
        # 10% nulos, outliers extremos, 5% duplicatas
        df = _adicionar_nulos(df, 0.10)
        df = _adicionar_outliers_pesados(df)
        df = _adicionar_duplicatas(df, 0.05)
        df = _inconsistencias_strings_pesadas(df)
        df = _adicionar_colunas_inuteis(df)  # colunas que devem ser removidas
    
    # Embaralhar linhas
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    
    return df

def _adicionar_nulos(df, prop):
    df_nulos = df.copy()
    colunas_numericas = ['sepal length (cm)', 'sepal width (cm)', 
                         'petal length (cm)', 'petal width (cm)']
    
    for col in colunas_numericas:
        mask = np.random.random(len(df)) < prop
        df_nulos.loc[mask, col] = np.nan
        
    # Nulos também na espécie (5% dos nulos totais)
    mask_species = np.random.random(len(df)) < (prop * 0.5)
    df_nulos.loc[mask_species, 'species_name'] = np.nan
    
    return df_nulos

def _adicionar_outliers_moderados(df):
    df_out = df.copy()
    # Petal length: alguns valores muito altos
    mask = np.random.random(len(df)) < 0.03
    df_out.loc[mask, 'petal length (cm)'] = df_out.loc[mask, 'petal length (cm)'] * 3
    
    # Sepal width: alguns valores negativos (impossível!)
    mask = np.random.random(len(df)) < 0.02
    df_out.loc[mask, 'sepal width (cm)'] = -df_out.loc[mask, 'sepal width (cm)']
    
    return df_out

def _adicionar_duplicatas(df, prop):
    n_duplicatas = int(len(df) * prop)
    duplicatas = df.sample(n_duplicatas, replace=True)
    return pd.concat([df, duplicatas], ignore_index=True)

def _inconsistencias_strings_medias(df):
    df_str = df.copy()
    # Versões diferentes da mesma espécie
    substituicoes = {
        'setosa': ['Setosa', 'SETOSA', 'setoza', 'Setoza'],
        'versicolor': ['Versicolor', 'VERSICOLOR', 'versicolour', 'Versicolour'],
        'virginica': ['Virginica', 'VIRGINICA', 'virgínica', 'Virginic']
    }
    
    for original, variantes in substituicoes.items():
        mask = df_str['species_name'] == original
        n_variantes = mask.sum()
        for i, variante in enumerate(variantes):
            if i >= n_variantes // len(variantes):
                break
            idx = df_str[mask].index[i * len(variantes)]
            df_str.loc[idx, 'species_name'] = variante
            
    return df_str

def _adicionar_colunas_inuteis(df):
    # Simula colunas que um banco de dados real teria
    df['id_registro'] = range(len(df))
    df['data_coleta'] = pd.date_range('2024-01-01', periods=len(df), freq='D')
    df['observacao'] = np.random.choice(['', 'ok', 'revisar', 'suspeito'], len(df))
    df['temp_medida'] = np.random.uniform(18, 30, len(df))  # temperatura irrelevante
    return df


# Gerar versão suja
df_sujo = criar_iris_sujo(nivel='medio')

# Problemas que os alunos vão encontrar:
print("=== DIAGNÓSTICO DO IRIS SUJO ===\n")

print(f"1. Shape: {df_sujo.shape}")
print(f"   - Original: 150 linhas")
print(f"   - Agora: {len(df_sujo)} linhas (com duplicatas)")

print(f"\n2. Valores ausentes:")
print(df_sujo.isnull().sum())

print(f"\n3. Outliers detectados:")
for col in ['sepal length (cm)', 'sepal width (cm)', 
            'petal length (cm)', 'petal width (cm)']:
    Q1 = df_sujo[col].quantile(0.25)
    Q3 = df_sujo[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df_sujo[col] < (Q1 - 1.5 * IQR)) | 
                (df_sujo[col] > (Q3 + 1.5 * IQR))).sum()
    print(f"   - {col}: {outliers} outliers")

print(f"\n4. Inconsistências nas espécies:")
print(df_sujo['species_name'].value_counts())

print(f"\n5. Duplicatas: {df_sujo.duplicated().sum()}")