import csv
import plotly.express as pl 

with open('data.csv') as f:
    df = csv.DictReader(f)
    figure = pl.scatter(df,x="Days Present",y="Marks In Percentage")
    figure.show()