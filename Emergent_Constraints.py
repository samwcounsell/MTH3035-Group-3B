import numpy
import pandas as pd
from scipy.stats import linregress

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("DataSet.csv")
difference = pd.read_csv("Difference.csv")
emergent_constraint = pd.read_csv("Slope.csv")

september_trend = emergent_constraint
march_trend = emergent_constraint

names = df.columns.tolist()
years = df.loc[0:35, "Year"].to_numpy()

ra_years = df.loc[4:35, "Year"].to_numpy()

sep_trend = df.loc[0:35,]

ra = sep_trend

for i in range(1,37):

    sep_trend[names[i]] = sep_trend[names[i]] - sep_trend[names[i]].mean()

    b = sep_trend[names[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(years, b))

    y = x[0]
    print(y)

    september_trend.loc[0, names[i]] = y

september_trend = september_trend.drop(['Year', 'Month'], axis = 1)

for i in range(1, 37):
    ra[names[i]] = ra.iloc[:, i].rolling(window=5).mean()

for i in range(1,37):

    ra[names[i]] = ra[names[i]] - ra[names[i]].mean()

    b = ra[names[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(ra_years, b))

    y = x[0]
    print(y)

    ra.loc[0, names[i]] = y

#september_trend.to_csv("september_trend.csv")

ra.to_csv("Hey.csv")

mar_trend = df.loc[36:71,]

for i in range(1,37):

    mar_trend[names[i]] = mar_trend[names[i]] - mar_trend[names[i]].mean()

    b = mar_trend[names[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(years, b))

    y = x[0]
    print(y)

    march_trend.loc[0, names[i]] = y

march_trend = march_trend.drop(['Year', 'Month'], axis = 1)

#march_trend.to_csv("march_trend.csv")