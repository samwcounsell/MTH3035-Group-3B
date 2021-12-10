import plotly.express as px
import pandas as pd

df = px.data.wind()
print(df)

polar_df = pd.read_csv("polar_df.csv")
print(polar_df)

colors = ["navy", "navy", "navy", "navy", "navy", "navy", "blue", "blue", "blue", "blue", "blue", "blue",
          "cornflowerblue", "cornflowerblue", "cornflowerblue", "cornflowerblue", "cornflowerblue", "cornflowerblue",
          "lightgray", "lightgray", "lightgray", "lightgray", "lightgray", "lightgray", "plum", "plum", "plum", "plum",
          "plum", "plum", "violet", "violet", "violet", "violet", "violet", "violet", "hotpink", "hotpink", "hotpink",
          "hotpink", "hotpink", "hotpink", "hotpink"]

fig = px.line_polar(polar_df, r="extent", theta="mo", line_close=True,
                    color="Year",
                    color_discrete_sequence=colors)
fig.update_layout(
    title = "Polar Line Chart showing observed sea ice extent from 1979 - 2020 (Million km\N{SUPERSCRIPT TWO})",
    title_x=0.5,
    font_size = 21,
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

fig.show()

fig_a = px.line_polar(polar_df, r="area", theta="mo", line_close=True,
                    color="Year",
                    color_discrete_sequence=colors)
fig_a.update_layout(
    title = "Polar Line Chart showing observed sea ice area from 1979 - 2020 (Million km\N{SUPERSCRIPT TWO})",
    title_x=0.5,
    font_size = 21,
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
fig_a.show()
