import numpy
import numpy as np
import pandas as pd
import plotly.express as px
from scipy.stats import linregress


#df = pd.read_csv("MarVSep/DataSet.csv")
#difference = pd.read_csv("MarVSep/Difference.csv")

df = pd.read_csv("DataSet.csv")
difference = pd.read_csv("Difference.csv")
slope = pd.read_csv("Slope.csv")

ra = df
ra_difference = difference


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

names = df.columns.tolist()

for i in range(1,37):
    for j in range(0,36):
        sep = df.iloc[j, i]
        #print(sep)
        mar = df.iloc[j + 36, i]
        #print(mar)
        diff = mar - sep
        #print(diff)

        difference.iloc[j,i] = diff

#print(difference)

df2 = pd.melt(difference, id_vars="Year",
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
#print(df2)

df2 = df2.rename(columns={"variable": "Model", "value": "Difference"})

#print(df2)

blues = ["red", "indigo", "darkslateblue", "darkblue", "navy", "blue", "indigo", "hotpink", "dodgerblue", "black",
         "darkorchid", "mediumpurple", "violet", "darkslateblue", "darkblue", "navy", "blue", "indigo",
         "hotpink", "dodgerblue", "black", "darkorchid", "mediumpurple", "violet", "darkslateblue",
         "darkblue", "navy", "blue", "indigo", "hotpink", "dodgerblue", "black", "darkorchid",
         "mediumpurple", "violet", "darkslateblue", "darkblue"]

MvS = px.line(df2, x="Year", y="Difference", color="Model", color_discrete_sequence=blues)
MvS.update_xaxes(
    range=[1979, 2014]
)
MvS.update_layout(
    title="Difference between March and September sea ice levels from 1979 - 2014",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Difference (Million km^2)")
MvS.show()
MvS.update_layout(xaxis_range=[1979, 2014])

### Rolling Average Differnce


for i in range(1, 37):
    ra[names[i]] = ra.iloc[:, i].rolling(window=5).mean()

anom = ra
anom_difference = ra_difference

for i in range(1,37):
    for j in range(0,36):
        sep = ra.iloc[j, i]
        mar = ra.iloc[j + 36, i]
        diff = mar - sep

        ra_difference.iloc[j,i] = diff

#print(ra_difference)

ra2 = pd.melt(ra_difference, id_vars="Year",
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

ra2 = ra2.rename(columns={"variable": "Model", "value": "Difference"})

#print(ra2)

raMvS = px.line(ra2, x="Year", y="Difference", color="Model", color_discrete_sequence=blues)
raMvS.update_xaxes(
    range=[1983, 2014]
)
raMvS.update_layout(
    title="5 Year Rolling Average Difference between March and September sea ice levels from 1983 - 2014",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Difference (Million km^2)")
raMvS.show()
raMvS.update_layout(xaxis_range=[1983, 2014])

###### Rolling Average variation from mean

a = anom_difference["Year"].to_numpy()
a = np.delete (a, [0,1,2,3])

print(a)


for i in range(1,37):

    anom_difference[names[i]] = anom_difference[names[i]] - anom_difference[names[i]].mean()

    b = anom_difference[names[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(a, b))
    #print(names[i], x)

    y = x[0]
    print(y)

    slope.loc[0, names[i]] = y
    print(slope)

#print(anom_difference)

anomra2 = pd.melt(anom_difference, id_vars="Year",
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

anomra2 = anomra2.rename(columns={"variable": "Model", "value": "Difference"})

anomraMvS = px.line(anomra2, x="Year", y="Difference", color="Model", color_discrete_sequence=blues)
anomraMvS.update_xaxes(
    range=[1983, 2014]
)
anomraMvS.update_layout(
    title="Yearly anomaly in 5 Year Rolling Average Difference between March and September sea ice levels from 1983 - 2014",
    xaxis_title="Year",
    yaxis_title="Sea Ice Extent Difference Anomaly (Million km^2)")
anomraMvS.show()
anomraMvS.update_layout(xaxis_range=[1983, 2014])

slope.to_csv("MarvSep_Anomaly_LinearRegression_Gradients.csv")