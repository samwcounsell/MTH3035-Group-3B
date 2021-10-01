import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

Mar_Sep_Data = pd.read_csv('N03N09Extent.csv')

Ext_Graph = px.line(Mar_Sep_Data, x="Year", y="Extent", title='March/Septmeber Sea Ice Extent', color='Month', color_discrete_sequence=["cyan", "blue"])
Area_Graph = px.line(Mar_Sep_Data, x="Year", y="Area", title='March/September Sea Ice Area', color='Month', color_discrete_sequence=["cyan", "blue"])

# CMIP6 Sep Data

CMIP6_Sep_Data = pd.read_csv('CMIP6_Sep_SIA_X.csv')

CMIP6_Area_Graph = px.line(CMIP6_Sep_Data, x="Year", y="SIA", title='CMPI6 September Sea Ice Area Model Comparison', color='Model', color_discrete_sequence=["cyan", "blue", "magenta"])

external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = html.Div([
    dbc.Row(dbc.Col(html.H1("March/September Sea Ice Graphs"),
                    width={'size': 10, 'offset': 3},
                    ),
            ),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=Ext_Graph, style={'display': 'inline-block'}),
                width={'size': 6, 'offset': 0},
                ),
        dbc.Col(dcc.Graph(figure=Area_Graph, style={'display': 'inline-block'}),
                width=6,
                ),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=CMIP6_Area_Graph, style={'width': '160vh', 'height': '50vh'}),
                width={'size': 12, 'offset': 0},
                ),
    ]),
])




app.run_server(debug=True)