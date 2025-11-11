import pandas as pd

data= pd.read_csv ("air_quality_health_dataset.csv")

#a) There are only 2 categorical data
print(pd.crosstab(data["city"],data["population_density"]))
#b)
print(pd.crosstab(data["city"],data["population_density"], normalize=True))
#c) We cannot do a three-way table because we only have 2 categorical data
