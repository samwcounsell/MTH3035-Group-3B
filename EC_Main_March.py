import numpy
import pandas as pd
import scipy
from scipy.stats import linregress
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.metrics import r2_score


df = pd.read_csv("march_trend.csv")

df = df.head(4)

df = df.set_index('Model').T

df = df.fillna(0)

df126 = df["ssp126"] > 0

df_mask126=df['ssp126']>0
df126 = df[df_mask126]

l126 = df126['ssp126'].to_numpy()
l126t = df126['Trend'].to_numpy()

slope126, intercept126, r_value126, p_value126, std_err126 = scipy.stats.linregress(l126, l126t)

print(r_value126)

df245 = df["ssp245"] > 0

df_mask245=df['ssp245']>0
df245 = df[df_mask245]

l245 = df245['ssp245'].to_numpy()
l245t = df245['Trend'].to_numpy()

slope245, intercept245, r_value245, p_value245, std_err245 = scipy.stats.linregress(l245, l245t)

print(r_value245)

df585 = df["ssp585"] > 0

df_mask585=df['ssp585']>0
df585 = df[df_mask585]

l585 = df585['ssp585'].to_numpy()
l585t = df585['Trend'].to_numpy()

slope585, intercept585, r_value585, p_value585, std_err585 = scipy.stats.linregress(l585, l585t)

print(r_value585)

fig126 = px.scatter(df126, x="ssp126", y="Trend", trendline="ols")
fig126.show()

fig126 = px.scatter(df126, x="ssp126", y="Trend", trendline="ols")
fig126.show()

fig585 = px.scatter(df585, x="ssp585", y="Trend", trendline="ols")
fig585.show()