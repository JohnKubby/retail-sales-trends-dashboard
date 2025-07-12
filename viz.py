
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

app = Dash(__name__)

# Load data
region_df = pd.read_csv('../data/regional_sales.csv')
category_df = pd.read_csv('../data/product_sales.csv')

# Create regional line chart
region_fig = px.line(region_df, x="Year", y="Sales", color="Region", markers=True,
                     title="Online Retail Sales by Region (2018–2023)")

# Create product category bar chart
category_fig = px.bar(category_df, x="Year", y="Sales", color="Category", barmode="stack",
                      title="Online Retail Sales by Product Category (2018–2023)")

# Layout
app.layout = html.Div(children=[
    html.H1("Online Retail Sales Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(figure=region_fig),
    dcc.Graph(figure=category_fig)
])

if __name__ == '__main__':
    app.run_server(debug=False)
