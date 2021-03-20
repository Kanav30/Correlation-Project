#here we import all the libraries
import numpy as np
import pandas as pd
import plotly.express as px
import csv

#here we get all the data in arrays and make them integers and stuff(not sure how to eplain it so)
def getdatasource(data):
    MarksInPercentage = []
    DaysPresent = []
    with open(data)as f:
        df = csv.DictReader(f)
        for ro in df:
            MarksInPercentage.append(float(ro["Marks In Percentage"])) 
            DaysPresent.append(float(ro["Days Present"]))
    
    return{"x":DaysPresent,"y":MarksInPercentage}

#funtion to find the correlation
def findcorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Days Present and Marks In Percentage: ", correlation[0,1])

#plotting the data on a scatter plot here
#i didnt know properly what to take on X-Axis and Y-Axis so i have commented the other possiblity
def plottingfig(data):
    with open(data)as a:
        df = csv.DictReader(a)
        fig = px.scatter(df,x='Days Present',y='Marks In Percentage')
        #fig = px.scatter(df,x='Marks In Percentage',y='Days Present')        
        fig.show()

#here we import the data file
def setup():
    data = "./Student Marks vs Days Present.csv"
    dataSource = getdatasource(data)
    findcorrelation(dataSource)
    plottingfig(data)

setup()