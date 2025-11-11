import pandas as pd

data= pd.read_csv ("air_quality_health_dataset.csv")

#a
print(data.head(5)) 
print(data.tail(5))
print(data.shape)
print(data.info())
print(data.describe())

#b
print(data.duplicated().drop_duplicates())

#c
print(pd.isnull(data).sum()) #There aren't any null values

#d
print(pd.to_datetime(data["date"]))