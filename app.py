
# IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# 1. CARREGAMENTO DOS DADOS

# Lê o dataset
df = pd.read_csv('ecommerce_estatistica.csv')

# Seleciona colunas usadas na análise
df_analise = df[['Marca', 'Preço', 'Qtd_Vendidos_Cod']]

# Agrupa vendas por marca
marcas_vendas = df_analise.groupby('Marca')['Qtd_Vendidos_Cod'].sum().sort_values(ascending=False)

# Top 10 marcas
top10_marcas = marcas_vendas.head(10).reset_index()


# 2. CRIAÇÃO DOS GRÁFICOS

# Gráfico de barras (Top 10 marcas)
fig_bar = px.bar(
    top10_marcas,
    x='Marca',
    y='Qtd_Vendidos_Cod',
    title='Top 10 Marcas Mais Vendidas'
)

# Dispersão (Preço vs vendas)
fig_scatter = px.scatter(
    df_analise,
    x='Preço',
    y='Qtd_Vendidos_Cod',
    title='Preço vs Quantidade Vendida'
)

# Histograma (preço)
fig_hist = px.histogram(
    df_analise,
    x='Preço',
    title='Distribuição de Preços'
)

# Pizza (Top 5 marcas)
fig_pie = px.pie(
    top10_marcas.head(5),
    names='Marca',
    values='Qtd_Vendidos_Cod',
    title='Participação das Top 5 Marcas'
)


# 3. CRIAÇÃO DO DASHBOARD

app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H1("Dashboard de Vendas E-commerce"),

    html.P("Análise de vendas por marca e relação entre preço e quantidade vendida."),

    # Gráficos
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_scatter),
    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_pie),
])

# 4. RODAR A APLICAÇÃO

if __name__ == '__main__':
    app.run(debug=True)