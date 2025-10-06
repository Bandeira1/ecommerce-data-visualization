#  E-commerce Data Visualization

Análise exploratória e visualização de dados de um dataset de e-commerce, utilizando **Python**, **Pandas**, **Matplotlib** e **Seaborn**.

O objetivo do projeto é compreender padrões de comportamento em produtos vendidos online — como notas, descontos, volumes de vendas e preços — por meio de gráficos estatísticos e técnicas de regressão.

---

##  Tecnologias Utilizadas

- **Python 3.11+**
- **Pandas** – manipulação e limpeza de dados  
- **Matplotlib** – criação de gráficos  
- **Seaborn** – visualização estatística aprimorada  
- **Jupyter / VS Code / PyCharm** – ambiente de desenvolvimento  

---

##  Etapas do Projeto

1. **Importação e limpeza dos dados**
   - Conversão de colunas numéricas
   - Remoção de caracteres especiais e conversão de unidades (ex: “+10mil” → 10000)
   - Tratamento de valores ausentes

2. **Análise Exploratória (EDA)**
   - Estatísticas descritivas
   - Correlação entre variáveis
   - Visualização de padrões

3. **Visualizações criadas**
   - Histograma – distribuição das notas  
   - Dispersão – relação entre preço e nota  
   - Mapa de calor – correlação entre variáveis numéricas  
   - Gráfico de barras – top 10 marcas mais vendidas  
   - Gráfico de pizza – distribuição por gênero de produto  
   - Densidade – distribuição de preços  
   - Regressão – relação entre desconto e quantidade vendida  

---

##  Exemplo de Insights

- Produtos **masculinos** representam a maior parte do catálogo analisado.  
- Há uma **correlação moderada** entre **preço** e **nota média**.  
- Descontos elevados tendem a impulsionar o número de vendas, conforme visto no gráfico de regressão.  

---

##  Aprendizados

Durante o desenvolvimento, foram reforçados conceitos de:
- Limpeza e padronização de dados no Pandas  
- Criação de visualizações estatísticas com Seaborn  
- Interpretação de correlações e relações entre variáveis  

---

##  Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Bandeira1/ecommerce-data-visualization.git
   cd ecommerce-data-visualization

2. Instale as dependências:
   ```bash
   pip install pandas matplotlib seaborn

3. Execute o script principal:
   python lab.py
