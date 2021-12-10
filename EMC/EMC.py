import numpy
import pandas as pd
from scipy.stats import linregress

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

ssp126 = pd.read_csv("ssp126.csv")
ssp245 = pd.read_csv("ssp245.csv")
ssp585 = pd.read_csv("ssp585.csv")
# difference = pd.read_csv("Difference.csv")
emergent_constraint = pd.read_csv("Slope.csv")

september_trend126 = emergent_constraint
september_trend245 = emergent_constraint
september_trend585 = emergent_constraint


names126 = ssp126.columns.tolist()
names245 = ssp245.columns.tolist()
names585 = ssp585.columns.tolist()
years = ssp126.loc[0:20, "Year"].to_numpy()

sep_trend126 = ssp126.loc[0:20,]

for i in range(1,25):

    sep_trend126[names126[i]] = sep_trend126[names126[i]] - sep_trend126[names126[i]].mean()

    b = sep_trend126[names126[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(years, b))

    y = x[0]
    print(y)

    september_trend126.loc[0, names126[i]] = y

september_trend126 = september_trend126.drop(['Year', 'Month'], axis = 1)

print(september_trend126)

september_trend126.to_csv("126_trend.csv")




sep_trend245 = ssp245.loc[0:20,]

for i in range(1,27):

    sep_trend245[names245[i]] = sep_trend245[names245[i]] - sep_trend245[names245[i]].mean()

    b = sep_trend245[names245[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(years, b))

    y = x[0]
    print(y)

    september_trend245.loc[0, names245[i]] = y

september_trend245 = september_trend245.drop(['Year', 'Month'], axis = 1)

print(september_trend245)

september_trend245.to_csv("245_trend.csv")




sep_trend585 = ssp585.loc[0:20,]

for i in range(1,26):

    sep_trend585[names585[i]] = sep_trend585[names585[i]] - sep_trend585[names585[i]].mean()

    b = sep_trend585[names585[i]].to_numpy()
    b = b[~numpy.isnan(b)]

    x = (linregress(years, b))

    y = x[0]
    print(y)

    september_trend585.loc[0, names585[i]] = y

september_trend585 = september_trend585.drop(['Year', 'Month'], axis = 1)

print(september_trend585)

september_trend585.to_csv("585_trend.csv")






