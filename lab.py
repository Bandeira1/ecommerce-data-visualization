# =======================================
# 📊 Análise de Dados de E-commerce
# Autor: Victor Bandeira
# =======================================

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import re

# ==============================
# 1. Leitura e limpeza dos dados
# ==============================
df = pd.read_csv('ecommerce_estatistica.csv')

# --- Limpeza de Qtd_Vendidos usando regex + lambda ---
df['Qtd_Vendidos'] = (
    df['Qtd_Vendidos']
    .astype(str)
    .str.lower()
    .apply(lambda x: int(re.sub(r'\D', '', x)) * 1000 if 'mil' in x else int(re.sub(r'\D', '', x))
           if re.sub(r'\D', '', x) else None)
)

# --- Conversão de colunas numéricas ---
colunas_numericas = ['Nota', 'N_Avaliações', 'Desconto', 'Preço']
df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')

print(df.info())
print(df.head())


# ==============================
# 2. Funções de Visualização
# ==============================

def plota_histograma(df):
    """1️⃣ Gráfico de Histograma"""
    plt.figure(figsize=(10,6))
    sns.histplot(df['Nota'], bins=20, kde=False, color="blue")
    plt.title("Distribuição das Notas")
    plt.xlabel("Notas")
    plt.ylabel("Frequência")
    plt.show()


def plota_dispersao(df):
    """2️⃣ Gráfico de Dispersão"""
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x="Preço", y="Nota", hue="Desconto", alpha=.7, palette="Greens")
    plt.title("Dispersão: Preço x Nota (com Desconto)")
    plt.xlabel("Preço (R$)")
    plt.ylabel("Nota")
    plt.show()


def plota_heatmap(df):
    """3️⃣ Mapa de Calor"""
    plt.figure(figsize=(10,6))
    df_corr = df[['Nota','N_Avaliações','Desconto','Qtd_Vendidos','Preço']].corr()
    sns.heatmap(df_corr, annot=True, cmap="YlGnBu", fmt='.2f')
    plt.title('Mapa de Calor das Correlações')
    plt.show()


def plota_barras(df):
    """4️⃣ Gráfico de Barras"""
    plt.figure(figsize=(10,6))
    top_marcas = df['Marca'].value_counts().head(10)
    sns.barplot(x=top_marcas.values, y=top_marcas.index, color="skyblue")
    plt.title('Top 10 Marcas mais Vendidas')
    plt.xlabel('Quantidade de Produtos')
    plt.ylabel('Marcas')
    plt.show()


def plota_pizza(df):
    """5️⃣ Gráfico de Pizza"""
    genero_counts = df['Gênero'].value_counts()
    genero_top = genero_counts.head(4)
    plt.figure(figsize=(7,7))
    plt.pie(genero_top, labels=genero_top.index, autopct='%1.1f%%', startangle=90)
    plt.title("Top 4 Gêneros de Produtos")
    plt.show()


def plota_densidade(df):
    """6️⃣ Gráfico de Densidade"""
    plt.figure(figsize=(10,6))
    sns.kdeplot(df['Preço'], fill=True, color='red')
    plt.title('Densidade de Preços')
    plt.xlabel('Preço (R$)')
    plt.show()


def plota_regressao(df):
    """7️⃣ Gráfico de Regressão"""
    plt.figure(figsize=(10,6))
    sns.regplot(x='Desconto', y='Qtd_Vendidos', data=df, color='red',
                scatter_kws={'alpha': 0.5, 'color': '#34c289'})
    plt.title("Regressão: Desconto x Quantidade Vendida")
    plt.xlabel("Desconto (%)")
    plt.ylabel("Qtd_Vendidos")
    plt.show()


# ==============================
# 3. Execução dos 7 gráficos
# ==============================
plota_histograma(df)
plota_dispersao(df)
plota_heatmap(df)
plota_barras(df)
plota_pizza(df)
plota_densidade(df)
plota_regressao(df)
