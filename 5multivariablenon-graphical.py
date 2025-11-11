import pandas as pd

data= pd.read_csv ("air_quality_health_dataset.csv")

print(pd.crosstab(data["city"],data["population_density"]))

print(pd.crosstab(data["city"],data["population_density"], normalize=True))