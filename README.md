# Análise de Dados e Dashboard de E-commerce

Este projeto tem como objetivo realizar uma análise exploratória de dados de um e-commerce e disponibilizar os resultados por meio de um dashboard interativo.

---

## Objetivo

Analisar o comportamento de vendas dos produtos, com foco em:

* Identificar as marcas mais vendidas
* Entender a relação entre preço e quantidade vendida
* Explorar padrões e distribuições dos dados

---

## Estrutura do Projeto

```
analise-ecommerce/
│
├── analise_ecommerce.ipynb   # Notebook com análise exploratória
├── app.py                    # Dashboard interativo com Dash
├── ecommerce_estatistica.csv # Base de dados
└── README.md                 # Documentação do projeto
```

---

## Análise Exploratória

A análise foi realizada utilizando Python e as bibliotecas:

* Pandas
* Seaborn
* Matplotlib

### Principais etapas:

* Verificação de tipos de dados
* Identificação de valores nulos
* Estatísticas descritivas
* Agrupamento de dados por marca

---

## Visualizações Criadas

Foram desenvolvidos os seguintes gráficos:

* Histograma (Distribuição de preços)
* Gráfico de dispersão (Preço vs Quantidade vendida)
* Mapa de calor (Correlação entre variáveis)
* Gráfico de barras (Top 10 marcas mais vendidas)
* Gráfico de pizza (Participação das principais marcas)
* Gráfico de densidade
* Gráfico de regressão

---

## Principais Insights

* Algumas marcas concentram a maior parte das vendas
* Existe relação entre preço e quantidade vendida
* A distribuição de preços apresenta padrões específicos
* Possíveis outliers foram identificados na base de dados

---

## Dashboard Interativo

O projeto também conta com um dashboard desenvolvido com Dash, permitindo a visualização interativa dos dados.

### Como executar o projeto

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/analise-ecommerce.git
```

2. Acesse a pasta:

```
cd analise-ecommerce
```

3. Instale as dependências:

```
pip install dash plotly pandas
```

4. Execute a aplicação:

```
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:8050/
```

---

## Tecnologias Utilizadas

* Python
* Pandas
* Seaborn
* Matplotlib
* Dash
* Plotly

---

## Considerações Finais

Este projeto foi desenvolvido com o objetivo de praticar análise de dados e construção de dashboards interativos, simulando um cenário real de negócio.

---

## Autor

Projeto desenvolvido por Rafael Crivelin
