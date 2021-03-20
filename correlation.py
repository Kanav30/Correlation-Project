#this is just to test the scatter graph
import pandas as pd
import plotly.express as px
import csv
df = pd.read_csv("Student Marks vs Days Present.csv")

fig = px.scatter(df,x='Days Present',y='Marks In Percentage')
fig.show()