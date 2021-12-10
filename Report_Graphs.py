import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.io as pio

template = pio.templates["simple_white"]

sep_df = pd.read_csv("Sep_Data.csv")
mar_df = pd.read_csv("Mar_Data.csv")

sep126_df = pd.read_csv("Sep126.csv")
sep245_df = pd.read_csv("Sep245.csv")
sep585_df = pd.read_csv("Sep585.csv")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Custom colour scheme
blues = ["crimson", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue", "cornflowerblue", "deepskyblue", "lightskyblue", "slateblue", "blue"]

names = sep_df.columns.tolist()

# Changing data to 5 year rolling average to reduce noise
for i in range(1, 37):
    sep_df[names[i]] = sep_df.iloc[:, i].rolling(window=5).mean()

# Melting the data by model to make data easier to plot in Plotly
sep_df_melt = pd.melt(sep_df, id_vars="Year", value_vars=names, ignore_index=False)
sep_df_melt = sep_df_melt.rename(columns={"variable": "Model", "value": "Sea Ice Extent"})

# Plotly figure for September Sea Ice Extent
sep_fig = px.line(sep_df_melt, x="Year", y="Sea Ice Extent", color="Model", color_discrete_sequence=blues)
sep_fig.update_xaxes(
    range=[1983, 2014]
)
sep_fig.update_layout(
    template=template,
    title="September Sea Ice Extent Model Comparison (5 Year Rolling Average)",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Million km\N{SUPERSCRIPT TWO})",
    font=dict(size=12)
)

# Changing data to 5 year rolling average to reduce noise
for i in range(1, 37):
    mar_df[names[i]] = mar_df.iloc[:, i].rolling(window=5).mean()

# Melting the data by model to make data easier to plot in Plotly
mar_df_melt = pd.melt(mar_df, id_vars="Year", value_vars=names, ignore_index=False)
mar_df_melt = mar_df_melt.rename(columns={"variable": "Model", "value": "Sea Ice Extent"})

# Plotly figure for martember Sea Ice Extent
mar_fig = px.line(mar_df_melt, x="Year", y="Sea Ice Extent", color="Model", color_discrete_sequence=blues)
mar_fig.update_xaxes(
    range=[1983, 2014]
)
mar_fig.update_layout(
    template=template,
    title="March Sea Ice Extent Model Comparison (5 Year Rolling Average)",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Million km\N{SUPERSCRIPT TWO})",
    font=dict(size=12)
)

ssp_names = names
del ssp_names[1]

# Melting the data by model to make data easier to plot in Plotly
sep126_df_melt = pd.melt(sep126_df, id_vars="Year", value_vars=ssp_names, ignore_index=False)
sep126_df_melt = sep126_df_melt.rename(columns={"variable": "Model", "value": "Sea Ice Extent"})

# Melting the data by model to make data easier to plot in Plotly
sep245_df_melt = pd.melt(sep245_df, id_vars="Year", value_vars=ssp_names, ignore_index=False)
sep245_df_melt = sep245_df_melt.rename(columns={"variable": "Model", "value": "Sea Ice Extent"})

# Melting the data by model to make data easier to plot in Plotly
sep585_df_melt = pd.melt(sep585_df, id_vars="Year", value_vars=ssp_names, ignore_index=False)
sep585_df_melt = sep585_df_melt.rename(columns={"variable": "Model", "value": "Sea Ice Extent"})

sep126_fig = px.line(sep126_df_melt, x="Year", y="Sea Ice Extent", title='CMPI6 September Sea Ice Area Model Comparison (ssp126)',
                           color='Model', color_discrete_sequence=["cornflowerblue"])
sep126_fig.update_layout(
    template=template,
    title="Model predictions for SSP126",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Million km\N{SUPERSCRIPT TWO})",
    font=dict(size=18),
    yaxis_range=[0, 10]
)
sep245_fig = px.line(sep245_df_melt, x="Year", y="Sea Ice Extent", title='CMPI6 September Sea Ice Area Model Comparison (ssp245)',
                           color='Model', color_discrete_sequence=["crimson"])
sep245_fig.update_layout(
    template=template,
    title="Model predictions for SSP245",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Million km\N{SUPERSCRIPT TWO})",
    font=dict(size=18),
    yaxis_range=[0,10]
)

sep585_fig = px.line(sep585_df_melt, x="Year", y="Sea Ice Extent", title='CMPI6 September Sea Ice Area Model Comparison (ssp585)',
                           color='Model', color_discrete_sequence=["goldenrod"])
sep585_fig.update_layout(
    template=template,
    title="Model predictions for SSP585",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Million km\N{SUPERSCRIPT TWO})",
    font=dict(size=18),
    yaxis_range = [0, 10]
)

polar_df = pd.read_csv("polar_df.csv")

colors = ["navy", "navy", "navy", "navy", "navy", "navy", "blue", "blue", "blue", "blue", "blue", "blue",
          "cornflowerblue", "cornflowerblue", "cornflowerblue", "cornflowerblue", "cornflowerblue", "cornflowerblue",
          "lightgray", "lightgray", "lightgray", "lightgray", "lightgray", "lightgray", "plum", "plum", "plum", "plum",
          "plum", "plum", "violet", "violet", "violet", "violet", "violet", "violet", "hotpink", "hotpink", "hotpink",
          "hotpink", "hotpink", "hotpink", "hotpink"]

fig_pe = px.line_polar(polar_df, r="extent", theta="mo", line_close=True,
                    color="Year",
                    color_discrete_sequence=colors)
fig_pe.update_layout(
    title = "Polar Line Chart showing observed sea ice extent from 1979 - 2020 (Million km\N{SUPERSCRIPT TWO})",
    font_size = 14,
    polar = dict(
      angularaxis = dict(
        linewidth = 3,
        showline=True,
        linecolor='black'
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = True,
        linewidth = 2,
        gridcolor = "white",
        gridwidth = 2,

      )
    ),
)

fig_a = px.line_polar(polar_df, r="area", theta="mo", line_close=True,
                    color="Year",
                    color_discrete_sequence=colors)
fig_a.update_layout(
    title = "Polar Line Chart showing observed sea ice area from 1979 - 2020 (Million km\N{SUPERSCRIPT TWO})",
    font_size = 14,
    polar = dict(
      angularaxis = dict(
        linewidth = 3,
        showline=True,
        linecolor='black'
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = True,
        linewidth = 2,
        gridcolor = "white",
        gridwidth = 2,

      )
    ),
)

# Dash App

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = html.Div([
    dbc.Row(dbc.Col(html.H1("Dashboard for analysing CMIP6 and Observed data for Arctic Sea Ice"),
                    width={'size': 10, 'offset': 1},
                    ),
            ),

    dbc.Row(dbc.Col(html.P("Created for use by group 3B (Hazel, Sana, Sam, Yat, Terry, Hannah, Christian, Priyanka)"),
                    width={'size': 10, 'offset': 1},
                    ),
            ),

    dbc.Row(dbc.Col(html.H4(""),
                    width={'size': 10, 'offset': 4},
                    ),
            ),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=sep_fig, style={'display': 'inline-block'}),
                width={'size': 6, 'offset': 0},
                ),
        dbc.Col(dcc.Graph(figure=mar_fig, style={'display': 'inline-block'}),
                width=6,
                ),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=sep126_fig),
               width={'size': 12, 'offset': 0},
               ),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=sep245_fig),
               width={'size': 12, 'offset': 0},
               ),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=sep585_fig),
               width={'size': 12, 'offset': 0},
               ),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_pe),
               width={'size': 6, 'offset': 0},
               ),
    dbc.Col(dcc.Graph(figure=fig_a),
               width={'size': 6, 'offset': 0},
               ),
    ]),
])

app.run_server(debug=True)