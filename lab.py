import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_estatistica.csv')

# Função para limpar a coluna de quantidade vendida
def limpa_vendidos(valor):
    if pd.isna(valor):
        return None
    valor = str(valor).lower().strip()
    valor = valor.replace("+", "")  # remove o "+"
    valor = valor.replace(".", "")  # remove pontos
    valor = valor.replace("mil", "000")  # converte "mil" em "000"
    try:
        return int(valor)
    except:
        return None


df['Qtd_Vendidos'] = df['Qtd_Vendidos'].apply(limpa_vendidos)

colunas_numericas = ['Nota', 'N_Avaliações', 'Desconto', 'Preço']
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print(df.info())
print(df.head())


# =======================================
# 1. Gráfico de Histograma (Notas)
# =======================================
plt.figure(figsize=(10,6))
sns.histplot(df['Nota'], bins=20, kde=False, color="blue")
plt.title("Distribuição das Notas")
plt.xlabel("Notas")
plt.ylabel("Frequência")
plt.show()

# =======================================
# 2. Gráfico de Dispersão (Preço x Notas)
# =======================================
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Preço", y="Nota", hue="Desconto", alpha=.7, palette="Greens")
plt.title("Dispersão: Preço x Nota")
plt.xlabel("Preço")
plt.ylabel("Nota")
plt.show()

# =======================================
# 3. Gráfico de Calor (Correlação entre Variaveis Numericas)
# =======================================
plt.figure(figsize=(10,6))
df_corr = df[['Nota','N_Avaliações','Desconto','Qtd_Vendidos','Preço']].corr()
sns.heatmap(df_corr, annot=True, cmap="YlGnBu", fmt='.2f')
plt.title('Mapa de Calor')
plt.show()

# =======================================
# 4. Gráfico de Barras (Top 10 Marcas Vendidas)
# =======================================
plt.figure(figsize=(10,6))
top_marcas = df['Marca'].value_counts().head(10)
sns.barplot(x=top_marcas.values, y=top_marcas.index, color="skyblue")
plt.title('Top 10 Marcas mais Vendidas')
plt.xlabel('Quantidade de Produtos')
plt.ylabel('Marcas')
plt.show()

# =======================================
# 5. Gráfico de Pizza (Top 10 Marcas Vendidas)
# =======================================
genero_counts = df['Gênero'].value_counts()
genero_top = genero_counts.head(4)
plt.figure(figsize=(7,7))
plt.pie(genero_top, labels=genero_top.index, autopct='%1.1f%%', startangle=90)
plt.title("Top 4 Gêneros de Produtos")
plt.show()

# =======================================
# 6. Gráfico de Densidade (Preço)
# =======================================
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'], fill=True, color='Red')
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.show()

# =======================================
# 7. Gráfico de Regressão (Desconto x Vendas)
# =======================================
plt.figure(figsize=(10,6))
sns.regplot(x='Desconto', y='Qtd_Vendidos', data=df, color= 'red', scatter_kws={'alpha': 0.5, 'color':'#34c289'})
plt.xlabel('Desconto')
plt.ylabel('Qtd_Vendidos')
plt.show()

