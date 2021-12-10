import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("MD.csv")

ra = df

names = ra.columns.tolist()
figures = []

# for i in range(2, 37):
# for j in range(0, ra.shape[0], -2):
# ra.loc[ra.index[j + 2], names[i]] = np.round(
# ((ra.iloc[j - 2, i] + ra.iloc[j - 1, i] + ra.iloc[j, i] + ra.iloc[j + 1, i] + ra.iloc[j + 2, i]) / 5), 1)

for i in range(1, 37):
    ra[names[i]] = ra.iloc[:, i].rolling(window=5).mean()

print(ra)

#######
from scipy.stats import ks_2samp

#oe = ra["Observed_Extent"].to_numpy()

#for i in range(3, 38):
#    y = ra[names[i]].to_numpy()
#    ts = ks_2samp(oe, y)
#
#print(ts)
#######
ram = pd.melt(ra, id_vars="Year",
              value_vars=["Observed", "ACCESS-CM2", "ACCESS-ESM1-5", "AWI-CM-1-1-MR", "BCC-CSM2"
                                                                                             "-MR",
                          "BCC-ESM1",
                          "CAMS-CSM1-0",
                          "CESM2",
                          "CESM2-WACCM", "CNRM-CM6-1", "CNRM-ESM2-1", "CanESM5", "E3SM-1-0", "EC-Earth3",
                          "EC-Earth3-Veg", "FGOALS-f3-L", "GFDL-CM4", "GFDL-ESM4", "GISS-E2-1-G", "GISS-E2-1-G-CC",
                          "GISS-E2-1-H", "HadGEM3-GC31-LL", "HadGEM3-GC31-MM", "INM-CM4-8", "INM-CM5-0", "IPSL-CM6A-LR",
                          "MIROC-ES2L", "MIROC6", "MPI-ESM1-2-HR", "MPI-ESM1-2-LR", "MRI-ESM2-0",
                          "NESM3", "NorCPM1", "NorESM2-LM", "SAM0-UNICON", "UKESM1-0-LL"], ignore_index=False)
print(ram)

blues = ["red", "darkslateblue", "darkblue", "navy", "blue", "aqua", "cadetblue", "dodgerblue", "lightskyblue",
         "lightsteelblue", "mediumpurple", "powderblue", "darkslateblue", "darkblue", "navy", "blue", "aqua",
         "cadetblue", "dodgerblue", "lightskyblue", "lightsteelblue", "mediumpurple", "powderblue", "darkslateblue",
         "darkblue", "navy", "blue", "aqua", "cadetblue", "dodgerblue", "lightskyblue", "lightsteelblue",
         "mediumpurple", "powderblue", "darkslateblue", "darkblue"]

fig = px.line(ram, x="Year", y="value", color="variable", color_discrete_sequence=blues)
fig.update_xaxes(
    range=[1983, 2014]
)
fig.update_layout(
    title="Rolling 5 year average for model and observed sea ice extent",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent (Million km^2)")
fig.show()
fig.update_layout(xaxis_range=[1983, 2014])

