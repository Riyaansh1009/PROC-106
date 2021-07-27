import csv
import numpy as np

def setup():
    dataPath = "data.csv"
    data = getData(dataPath)
    findCorrelation(data)

def getData(path):
    x=[]
    y=[]
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for i in reader:
            x.append(float(i["Days Present"]))
            y.append(float(i["Marks In Percentage"]))
    return {"x":x,"y":y}
 
def findCorrelation(data):
    result = np.corrcoef(data["x"], data["y"])
    print("The correlation between the number of days present and the number of marks is", result)